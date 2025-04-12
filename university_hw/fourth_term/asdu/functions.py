import math
from math import log


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


def calc_lambda(re: float, d: float, roughness: float, use_colebrook_white=False, accuracy=10e6):
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
