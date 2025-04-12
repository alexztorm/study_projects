import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ================== ПАРАМЕТРЫ СИСТЕМЫ ==================
D_mm = 820  # мм
delta_mm = 9  # мм
sher_mm = 0.10  # мм
x0_km = 0  # км
xN_km = 111.89  # км
rho20 = 858.50  # кг/м³
nu20_cSt = 8.35  # сСт
nu50_cSt = 2.69  # сСт
Pn_MPa = 5.06  # МПа
Pk_MPa = 0.87  # МПа
T_C = 11.50  # °C
segments = 100  # число сегментов
time_mod = 100.0  # время моделирования, сек
output_interval = 0.1  # интервал визуализации, сек

# ================== ПЕРЕВОД В СИ ==================
D = D_mm / 1000  # м
delta = delta_mm / 1000  # м
sher = sher_mm / 1000  # м
x0 = x0_km * 1000  # м
xN = xN_km * 1000  # м
L = abs(xN - x0)  # м
dx = L / segments  # шаг по пространству
nu = nu20_cSt * 1e-6  # м²/с
Pn = Pn_MPa * 1e6  # Па
Pk = Pk_MPa * 1e6  # Па
T_K = T_C + 273.15  # K

# ================== СТАЦИОНАРНАЯ МОДЕЛЬ ==================
# Расчет стационарного распределения
pressure_stat = np.linspace(Pn, Pk, segments + 1)
velocity_stat = np.ones(segments + 1) * 1.5  # примерное значение

# Визуализация стационарного решения
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(np.linspace(x0, xN, segments + 1) / 1000, pressure_stat / 1e6)
plt.title('Стационарное распределение давления')
plt.xlabel('Расстояние, км')
plt.ylabel('Давление, МПа')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(np.linspace(x0, xN, segments + 1) / 1000, velocity_stat)
plt.title('Стационарное распределение скорости')
plt.xlabel('Расстояние, км')
plt.ylabel('Скорость, м/с')
plt.grid()
plt.tight_layout()
plt.show()

# ================== НЕСТАЦИОНАРНАЯ МОДЕЛЬ ==================
c = 1200  # Скорость звука
CFL = 0.9
dt = CFL * dx / c
num_steps = int(time_mod / dt)
skip_frames = max(1, int(output_interval // dt))

print(f"Шаг времени: {dt:.4f} с")
print(f"Всего шагов: {num_steps}")

x_points = np.linspace(x0, xN, segments + 1)
P = np.zeros((num_steps + 1, segments + 1))
V = np.zeros((num_steps + 1, segments + 1))

# Начальные условия
P[0, :] = np.linspace(Pn, Pk, segments + 1)
V[0, :] = np.ones(segments + 1) * 1.5

for n in range(num_steps):
    # Расчет инвариантов с правильными граничными условиями
    Ia = V[n, :] + P[n, :] / (rho20 * c)
    Ib = V[n, :] - P[n, :] / (rho20 * c)

    # Распространение инвариантов
    Ia[1:] = Ia[:-1]  # Ia движется вправо
    Ib[:-1] = Ib[1:]  # Ib движется влево

    # Граничные условия (постоянное давление на краях)
    Ia[0] = V[n, 0] + Pn / (rho20 * c)  # Левый край
    Ib[-1] = V[n, -1] - Pk / (rho20 * c)  # Правый край

    # Обновление параметров
    V[n + 1, :] = 0.5 * (Ia + Ib)
    P[n + 1, :] = 0.5 * rho20 * c * (Ia - Ib)

# ================== ВИЗУАЛИЗАЦИЯ ==================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.set_xlim(0, L / 1000)
ax1.set_ylim(Pk / 1e6 - 0.5, Pn / 1e6 + 0.5)
ax1.set_ylabel('Давление, МПа')
ax1.grid(True)

ax2.set_xlim(0, L / 1000)
ax2.set_ylim(1.0, 10.0)
ax2.set_xlabel('Расстояние, км')
ax2.set_ylabel('Скорость, м/с')
ax2.grid(True)

line_p, = ax1.plot([], [], 'b-', lw=2)
line_v, = ax2.plot([], [], 'r-', lw=2)
time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)


def init():
    line_p.set_data([], [])
    line_v.set_data([], [])
    time_text.set_text('')
    return line_p, line_v, time_text


def update(frame):
    n = frame * skip_frames
    if n >= num_steps:
        n = num_steps - 1

    line_p.set_data(x_points / 1000, P[n, :] / 1e6)
    line_v.set_data(x_points / 1000, V[n, :])
    time_text.set_text(f'Время: {n * dt:.2f} с')

    return line_p, line_v, time_text


ani = FuncAnimation(fig, update, frames=range(num_steps // skip_frames),
                    init_func=init, blit=True, interval=50)

plt.tight_layout()
plt.show()