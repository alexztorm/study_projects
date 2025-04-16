import numpy as np
from math import exp, sqrt
import matplotlib.pyplot as plt
import functions as f

# 1. Исходные данные
# Начальные параметры по вариантам
x_start = 0  # км, начало отрезка
x_end = 106.6  # км, конец отрезка
D = 630  # мм, внешний диаметр
delta = 8  # мм, толщина стенки
roughness = 0.18  # мм, абсолютная шероховатость
rho_20 = 842.4  # кг/м3, плотность при 20 оС
nu_20 = 25  # сСт, кинематическая вязкость при 20 оС
nu_50 = 4.4  # сСт, кинематическая вязкость при 50 оС
p_start = 5.48  # МПА, начальное давление
p_end = 0.92  # МПа, конечное давление
T = 5.8  # оС, температура

# Перевод в систему СИ
x_start = x_start * 1000  # м
x_end = x_end * 1000  # м
D = D / 1000  # м
delta = delta / 1000  # м
roughness = roughness / 1000  # м
nu_20 = nu_20 * 1e-6  # м2/с
nu_50 = nu_50 * 1e-6  # м2/с
p_start = p_start * 1e6  # Па
p_end = p_end * 1e6  # Па

# Начальные параметры, задающиеся пользователем
c = input('Введите значение скорость звука (с) - ')  # м/с, скорость звука

if not c:
    c = 1532.3
else:
    c = float(c)

n = input('Введите число сегментов - ')  # число сегментов моделирования

if not n:
    n = 1000
else:
    n = int(n)

dx = (x_end - x_start) / n  # шаг по пространству



# 2. Стационарная модель
# 2.1. Создание расчетной сетки модели с шагом dx
x = np.arange(x_start, x_end + dx / 10, dx).tolist()  # сетка расчетной модели

# 2.2. Вычисление реологии при расчетной температуре
rho = rho_20 * (1 + f.get_ksi(rho_20) * (20 - T))  # плотность при расчетной температуре
nu = nu_20 * exp(-f.get_K(nu_20, nu_50, 20, 50) * (T - 20))  # вязкость при расчетной температуре

# 2.3. Предварительный расчет (внутренний диаметр, длина трубы)
d = D - 2 * delta  # внутренний диаметр
L = abs(x_end - x_start)  # длина трубы

# 2.4. Итерации для вычисления скорости нефти (важно, она постоянная) по двум точкам
lmb = 0.02
v = sqrt(2 * abs(p_start - p_end) * d / (lmb * L * rho))
re = v * d / nu
new_lmb = f.calc_lambda(re, d, roughness)

while abs(new_lmb - lmb) > 1e-6:
    lmb = new_lmb
    v = sqrt(2 * abs(p_start - p_end) * d / (lmb * L * rho))
    re = v * d / nu
    new_lmb = f.calc_lambda(re, d, roughness)

x_km = [el / 1000 for el in x]  # сетка в км
p_mpa = [p_start - (p_start - p_end) * el / 1e6 for el in x]  # Давление вдоль трубопровода



# 3. Нестационарная модель
dt = dx / c  # c, шаг по времени по условию Куранта
time_segm = 1000  # количество шагов по времени
p_grid = np.zeros((n + 1, time_segm + 1))
v_grid = np.zeros((n + 1, time_segm + 1))

p_grid[:, 0] = [p_start - (p_start - p_end) * el for el in x]
v_grid[:, 0] = [v] * (n + 1)

for i in range(time_segm):
    Ia = v_grid[:, i] * (rho * c) + p_grid[:, i]
    Ib = p_grid[:, i] - v_grid[:, i] * (rho * c)

    Ia[1:] = Ia[:-1]
    Ib[:-1] = Ib[1:]

    Ia[0] = v_grid[i, 0] * (rho * c) + p_start
    Ib[-1] = p_end - v_grid[i, -1] * (rho * c)

    p_grid[:, i + 1] = (Ia + Ib) / 2
    v_grid[:, i + 1] = (Ia - Ib) / (2 * rho * c)

for row in v_grid:
    for el in row:
        print(el)

# Графики стационарного режима
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Стационарный режим')

ax[0].plot(x_km, p_mpa, label='Давление', color='blue')
ax[0].set_title('Изменение давления от расстояния')
ax[0].set_xlabel('Расстояние (км)')
ax[0].set_ylabel('Давление (МПа)')
ax[0].grid()
ax[0].legend()

ax[1].plot(x_km, [v] * (n + 1), label='Скорость', color='orange')
ax[1].set_title('Изменение скорости от расстояния')
ax[1].set_xlabel('Расстояние (км)')
ax[1].set_ylabel('Скорость (м/с)')
ax[1].grid()
ax[1].legend()

plt.tight_layout()
plt.show()

# Графики нестационарного режима
f.animate_non_stationary(L, time_segm, p_start, p_end, dt, x, p_grid, v_grid)
