import math
from types import SimpleNamespace
import matplotlib.pyplot as plt
from collections import deque

# ------------------------------------------------------------
# Конфигурация: геометрия, свойства среды и условия
# ------------------------------------------------------------
config = SimpleNamespace(
    # Геометрия трубопровода --------------------------------
    x_start_km=0.0,                     # [км] начальная точка
    x_end_km=122.5,                     # [км] конечная точка
    outer_d_mm=530.0,                   # [мм] наружный диаметр
    wall_th_mm=8.0,                     # [мм] толщина стенки
    abs_rough_mm=0.19,                  # [мм] абсолютная шероховатость
    
    # Условия работы ----------------------------------------
    temperature_c=27.80,                # [°C] эксплуатационная температура
    pressure_in_mpa=4.11,               # [МПа] входное давление
    pressure_out_mpa=0.53,              # [МПа] выходное давление
    
    # Свойства нефти ----------------------------------------
    density_ref=750.0,                  # [кг/м³] при 20°C и 1 атм
    compress_mod_pa=1300e6,             # [Па] модуль сжимаемости
    therm_exp_coeff=0.001118,           # [1/°C] коэф. теплового расширения
    kin_visc_t1=14.22e-6,               # [м²/с] при 20°C
    kin_visc_t2=5.90e-6,                # [м²/с] при 50°C
    t1=20.0,                            # [°C]
    t2=50.0,                            # [°C]
    c_sound=1000.0,                     # [м/с]
    
    # Численные параметры ----------------------------------
    segments=100,                       # число сегментов
    total_time_s=600.0,                 # [с] продолжительность моделирования
    save_interval_s=1.0                 # [с] интервал сохранения
)

# Преобразование единиц
config.length_m = (config.x_end_km - config.x_start_km) * 1e3
config.outer_d_m = config.outer_d_mm * 1e-3
config.wall_th_m = config.wall_th_mm * 1e-3
config.inner_d_m = config.outer_d_m - config.wall_th_m
config.abs_rough_m = config.abs_rough_mm * 1e-3

# Давления в Паскалях
p_in = config.pressure_in_mpa * 1e6
p_out = config.pressure_out_mpa * 1e6
def compute_density(cfg):
    """Плотность при T и p (линейная аппроксимация)."""
    avg_p = (p_in + p_out) / 2.0
    rho = cfg.density_ref * (
        1 + cfg.therm_exp_coeff * (20 - cfg.temperature_c)
        + (avg_p - 9.81e4) / cfg.compress_mod_pa
    )
    return rho

def compute_viscosity(cfg):
    """Кин. вязкость при заданной температуре по логарифмической зависимости."""
    k_coeff = math.log(cfg.kin_visc_t1 / cfg.kin_visc_t2) / (cfg.t2 - cfg.t1)
    visc = cfg.kin_visc_t1 * math.exp(-k_coeff * (cfg.temperature_c - cfg.t1))
    return visc, k_coeff

# Функция расчёта коэффициента трения
def friction_factor(Re, rel_rough):
    if Re < 2320:
        return 64.0 / Re  # ламинарный режим
    # турбулентный режим (Серхидес–Черчилль)
    A = -2.0 * math.log10(rel_rough / 3.7 + 12.0 / Re)
    B = -2.0 * math.log10(rel_rough / 3.7 + 2.51 * A / Re)
    Cc = -2.0 * math.log10(rel_rough / 3.7 + 2.51 * B / Re)
    return (A - (B - A)**2 / (Cc - 2.0*B + A))**-2

# ------------------------------------------------------------
# 1. Стационарная модель (расчёт скорости и профиля давления)
# ------------------------------------------------------------
def stationary_model(cfg):
    rho = compute_density(cfg)
    visc, _ = compute_viscosity(cfg)
    rel_rough = cfg.abs_rough_m / cfg.inner_d_m

    # Напорный уклон
    head = (p_in - p_out) / (rho * 9.81)
    S = 2 * 9.81 * head * cfg.inner_d_m / (1.05 * cfg.length_m)

    # Решение уравнения Дарси–Вейсбаха через бисекцию
    def target(v):
        Re = v * cfg.inner_d_m / visc
        f = friction_factor(Re, rel_rough)
        return f * v**2 - S

    left, right = 0.01, 10.0
    for _ in range(60):
        mid = 0.5 * (left + right)
        if target(left) * target(mid) <= 0:
            right = mid
        else:
            left = mid
        if abs(right - left) < 1e-6:
            break
    v_stat = 0.5 * (left + right)

    Re_final = v_stat * cfg.inner_d_m / visc
    f_final = friction_factor(Re_final, rel_rough)
    dpdx = f_final * rho * v_stat**2 / (2 * cfg.inner_d_m) + rho*v_stat**2*cfg.therm_exp_coeff/2
    # Профиль давления вдоль трубы
    dx = cfg.length_m / cfg.segments
    profile = [p_in - i * dpdx * dx for i in range(cfg.segments + 1)]
    return v_stat, f_final, profile

# ------------------------------------------------------------
# 2. Нестационарная модель (явная схема)
# ------------------------------------------------------------
def unsteady_model(cfg, v_stat, pressure_prof):
    rho = compute_density(cfg)
    visc, _ = compute_viscosity(cfg)
    dt = (cfg.length_m / cfg.segments) / cfg.c_sound
    N = int(cfg.total_time_s / dt)
    dx = cfg.length_m / cfg.segments

    # Граничные условия
    bc_left = {'type': 'pressure', 'schedule': [(0, p_in), (100, 0.8 * p_in)]}
    bc_right = {'type': 'pressure', 'schedule': [(0, p_out)]}

    def current_bc(bc, t):
        val = bc['schedule'][0][1]
        for t0, val0 in bc['schedule']:
            if t >= t0:
                val = val0
            else:
                break
        return val

    # Инициализация
    p = pressure_prof[:]
    v = [v_stat] * (cfg.segments + 1)
    lam = [friction_factor(v_stat * cfg.inner_d_m / visc, cfg.abs_rough_m / cfg.inner_d_m)] * (cfg.segments + 1)
    history = {'t': [], 'p': [], 'v': []}
    next_save = 0.0
    t = 0.0

    # Настройка графиков
    plt.ion()
    fig, (ax_p, ax_v) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    x_vals = [i * dx for i in range(cfg.segments + 1)]
    line_p_stat, = ax_p.plot(x_vals, pressure_prof, color='grey', linestyle='--', label='стац.')
    line_v_stat, = ax_v.plot(x_vals, [v_stat]*(cfg.segments+1), color='grey', linestyle='--', label='стац.')
    line_p_dyn, = ax_p.plot([], [], color='orange', linewidth=2, label='нест.')
    line_v_dyn, = ax_v.plot([], [], color='orange', linewidth=2, label='нест.')
    ax_p.set_ylabel('p, Па')
    ax_v.set_ylabel('v, м/с')
    ax_v.set_xlabel('x, м')
    ax_p.legend()
    ax_v.legend()
    fig.tight_layout()

    # Основной цикл
    for step in range(N):
        Ia = [0.0] * (cfg.segments + 1)
        Ib = [0.0] * (cfg.segments + 1)
        for i in range(1, cfg.segments + 1):
            Ia[i] = (p[i-1] + rho*cfg.c_sound*v[i-1]
                     - lam[i-1]*(rho*cfg.c_sound*v[i-1]*abs(v[i-1]))
                       / (2*cfg.inner_d_m)*dt)

        for i in range(cfg.segments):
            Ib[i] = (p[i+1] - rho*cfg.c_sound*v[i+1]
                     + lam[i+1]*(rho*cfg.c_sound*v[i+1]*abs(v[i+1]))
                       / (2*cfg.inner_d_m)*dt)

        p_new, v_new = p[:], v[:]
        for i in range(1, cfg.segments):
            p_new[i] = 0.5 * (Ia[i] + Ib[i])
            v_new[i] = 0.5 * (Ia[i] - Ib[i]) / (rho * cfg.c_sound)
        # Левая граница
        valL = current_bc(bc_left, t)
        if bc_left['type']=='pressure':
            p_new[0] = valL
            v_new[0] = (p_new[0] - Ib[0])/(rho*cfg.c_sound)
        else:
            v_new[0] = valL
            p_new[0] = Ia[0] - rho*cfg.c_sound*v_new[0]
        # Правая граница
        valR = current_bc(bc_right, t)
        if bc_right['type']=='pressure':
            p_new[-1] = valR
            v_new[-1] = (Ia[-1] - p_new[-1])/(rho*cfg.c_sound)
        else:
            v_new[-1] = valR
            p_new[-1] = rho*cfg.c_sound*v_new[-1] + Ib[-1]

        p, v = p_new, v_new
        t += dt
        if t >= next_save - 1e-12:
            history['t'].append(t)
            history['p'].append(p[:])
            history['v'].append(v[:])
            next_save += cfg.save_interval_s

        # Обновляем графики
        line_p_dyn.set_data(x_vals, p)
        line_v_dyn.set_data(x_vals, v)
        ax_p.relim(); ax_p.autoscale_view()
        ax_v.relim(); ax_v.autoscale_view()
        plt.pause(0.001)

    plt.ioff()
    plt.show()
    return history

# ------------------------------------------------------------
# Точка входа
# ------------------------------------------------------------
def main():
    v_stat, f_stat, p_profile = stationary_model(config)
    print(f"Velocity = {v_stat:.3f} m/s, Re = {v_stat*config.inner_d_m/compute_viscosity(config)[0]:.1f}")
    print(f"Friction factor = {f_stat:.4f}")
    print(f"Total ΔP = {(p_profile[0]-p_profile[-1]):.1f} Pa "
          f"≈ {(p_profile[0]-p_profile[-1])/1e5:.2f} bar")

    # Запуск нестационарной модели
    unsteady_model(config, v_stat, p_profile)

if __name__ == '__main__':
    main()
