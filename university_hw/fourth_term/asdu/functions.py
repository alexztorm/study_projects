import math
from math import log
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def get_ksi(rho: float) -> float:
    '''
    Вычисление коэффициента температурного объемного расширения жидкости
    для получения плотности при заданной температуре

    :param rho: плотность при стандартных условиях (температура +20 оС, давление атмосферное) [кг/м3]
    :return: коэффициент температурного объемного расширения жидкости [1/оС]
    '''

    rho_values = [720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940]
    ksi_values = [0.001183, 0.001118, 0.001054, 0.000995, 0.000937, 0.000882,
                  0.000831, 0.000782, 0.000734, 0.000688, 0.000645]

    for i, item in enumerate(rho_values):
        if rho < item:
            return ksi_values[i - 1]


def get_K(nu1: float, nu2: float, t1: float, t2: float) -> float:
    '''
    Вычисление коэффициента термовязкограммы (вискограммы) для получения
    кинематической вязкости при заданной температуре

    :param nu1: значение вязкости при температуре t1 (м2/с или сСт)
    :param nu2: значение вязкости при температуре t2 (м2/с или сСт)
    :param t1: температура (К или оС)
    :param t2: температура (К или оС)
    :return: коэффициент термовязкограммы (вискограммы) (1/К или 1/оС)
    '''

    return 1 / (t2 - t1) * log(nu1 / nu2)


def calc_lambda(re: float, d: float, roughness: float, use_colebrook_white=False, accuracy=1e6):
    if use_colebrook_white:
        lmbd = 0.04
        lmbd_new = 0.25 / (math.log10(roughness / (3.7 * d) + 5.74 / re ** 0.9)) ** 2

        while abs(lmbd - lmbd_new) > accuracy:
            lmbd = lmbd_new
            lmbd_new = 0.25 / (math.log10(roughness / (3.7 * d) + 5.74 / re ** 0.9)) ** 2

        return lmbd_new
    else:
        eps = roughness / d
        if re <= 2320:
            return 64 / re
        elif re <= 10000:
            gamma = 1 - math.exp(-0.002 * (re - 2320))
            return 64 / re * (1 - gamma) + 0.3164 / re ** 0.25 * gamma
        elif re <= 10 / eps:
            return 0.3164 / re ** 0.25
        elif re <= 500 / eps:
            return 0.11 * (eps + 68 / re) ** 0.25
        else:
            return 0.11 * eps ** 0.25


def animate_non_stationary(l: float, time_limit: int, p_start: float, p_end: float, dt: float, x, p, v, skip_frames=1):
    # ================== ВИЗУАЛИЗАЦИЯ ==================
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    ax1.set_xlim(0, l / 1000)
    ax1.set_ylim(p_end / 1e6 - 0.5, p_start / 1e6 + 0.5)
    ax2.set_xlabel('Расстояние, км')
    ax1.set_ylabel('Давление, МПа')
    ax1.grid(True)

    ax2.set_xlim(0, l / 1000)
    ax2.set_ylim(0.0, 1.0)
    ax2.set_xlabel('Расстояние, км')
    ax2.set_ylabel('Скорость, м/с')
    ax2.grid(True)

    line_p, = ax1.plot([], [], 'b-', lw=2)
    line_v, = ax2.plot([], [], 'r-', lw=2)
    time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)

    x = [el / 1000 for el in x]

    for row in p:
        for el in row:
            el = el / 1e6

    def init():
        line_p.set_data([], [])
        line_v.set_data([], [])
        time_text.set_text('')
        return line_p, line_v, time_text

    def update(frame):
        n = frame * skip_frames
        if n >= time_limit:
            n = time_limit - 1

        line_p.set_data(x, p[:, n])
        line_v.set_data(x, v[:, n])
        time_text.set_text(f'Время: {n * dt:.2f} с')

        return line_p, line_v, time_text

    ani = FuncAnimation(fig, update, frames=range(time_limit // skip_frames),
                        init_func=init, blit=True, interval=50)

    plt.tight_layout()
    plt.show()
