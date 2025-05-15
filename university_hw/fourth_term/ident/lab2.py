import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def EM_normix(dat, maxrepit=250, tolerance=1e-6, plotflag=False):
    """
    Оценка параметров модели Гауссовой смеси с двумя состояниями с помощью EM-алгоритма

    Параметры:
    dat - массив данных (n_samples,)
    maxrepit - максимальное число итераций (по умолчанию 250)
    tolerance - критерий остановки (по умолчанию 1e-6)
    plotflag - флаг для построения графиков (по умолчанию False)

    Возвращает:
    словарь с результатами:
    - loglike_undf_current: значения логарифмического правдоподобия
    - tol: изменения параметров на каждой итерации
    - state_probs: вероятности состояний
    - coef_estim: оценки параметров [mu1, mu2, std1, std2, p1, p2]
    - stopreason: причина остановки
    """
    T = len(dat)
    if dat.ndim > 1 and dat.shape[1] > 1:
        raise ValueError('Данные должны быть представлены вектор-столбцом')

    # Инициализация параметров
    emtemp_1 = np.mean(dat)
    emtemp_2 = np.mean(dat)
    estdtemp_1 = np.std(dat) - np.std(dat) / 4
    estdtemp_2 = np.std(dat)
    eptemp_1 = 0.3
    eptemp_2 = 1 - eptemp_1

    # Инициализация результатов
    results = {
        'loglike_undf_current': [],
        'tol': [np.inf],
        'stopreason': ''
    }

    l = 0
    while abs(results['tol'][l]) > tolerance and l < maxrepit:
        # E-шаг
        # Условные плотности для каждого состояния
        codf_current = np.zeros((T, 2))
        codf_current[:, 0] = norm.pdf(dat, loc=emtemp_1, scale=estdtemp_1)
        codf_current[:, 1] = norm.pdf(dat, loc=emtemp_2, scale=estdtemp_2)

        # Совместные плотности
        jddf_current = np.zeros((T, 2))
        jddf_current[:, 0] = eptemp_1 * codf_current[:, 0]
        jddf_current[:, 1] = eptemp_2 * codf_current[:, 1]

        # Безусловная плотность
        undf_current = jddf_current.sum(axis=1)

        # Вероятности состояний (апостериорные)
        iur_current = np.zeros((T, 2))
        iur_current[:, 0] = (eptemp_1 * codf_current[:, 0]) / undf_current
        iur_current[:, 1] = (eptemp_2 * codf_current[:, 1]) / undf_current

        # Логарифмическое правдоподобие
        results['loglike_undf_current'].append(np.sum(np.log(undf_current)))

        # M-шаг
        # Обновление средних
        emtemp_1_update = np.sum(dat * iur_current[:, 0]) / np.sum(iur_current[:, 0])
        emtemp_2_update = np.sum(dat * iur_current[:, 1]) / np.sum(iur_current[:, 1])

        # Обновление дисперсий
        estdtemp_1_update = np.sum((dat - emtemp_1) ** 2 * iur_current[:, 0]) / np.sum(iur_current[:, 0])
        estdtemp_2_update = np.sum((dat - emtemp_2) ** 2 * iur_current[:, 1]) / np.sum(iur_current[:, 1])

        # Обновление вероятностей
        eptemp_1_update = np.mean(iur_current[:, 0])
        eptemp_2_update = np.mean(iur_current[:, 1])

        # Проверка изменения параметров
        last = np.array([emtemp_1, emtemp_2, estdtemp_1, estdtemp_2, eptemp_1, eptemp_2])
        emtemp_1, emtemp_2 = emtemp_1_update, emtemp_2_update
        estdtemp_1, estdtemp_2 = np.sqrt(estdtemp_1_update), np.sqrt(estdtemp_2_update)
        eptemp_1, eptemp_2 = eptemp_1_update, eptemp_2_update
        current = np.array([emtemp_1, emtemp_2, estdtemp_1, estdtemp_2, eptemp_1, eptemp_2])

        # Евклидова норма изменения параметров
        results['tol'].append(np.sqrt(np.sum((last - current) ** 2)))

        l += 1

    # Причина остановки
    if l == maxrepit:
        results['stopreason'] = 'Причина останова: достижение максимального числа итераций'
    else:
        results['stopreason'] = 'Причина останова: достижение заданной точности'

    # Сохранение результатов
    results['state_probs'] = iur_current
    results['coef_estim'] = [emtemp_1, emtemp_2, estdtemp_1, estdtemp_2, eptemp_1, eptemp_2]

    # Визуализация
    if plotflag:
        plt.figure(figsize=(10, 8))

        # Режимы
        plt.subplot(2, 1, 1)
        inf_mean = np.where(iur_current[:, 0] > 0.5, emtemp_1, emtemp_2)
        plt.plot(dat, '-b', linewidth=2, label='Данные')
        plt.plot(inf_mean, '-g', linewidth=1, label='Оценка среднего')
        plt.title('Выход для ненаблюдаемого режима')
        plt.legend(loc='best')

        # Плотности
        plt.subplot(2, 1, 2)
        gridi = np.linspace(np.min(dat), np.max(dat), 200)
        kernel_density = norm.pdf(gridi, loc=np.mean(dat), scale=np.std(dat))
        kernel_density = kernel_density / np.max(kernel_density)
        plt.plot(gridi, kernel_density, '-b', linewidth=2, label='Оценка ядра')

        # Гауссовская смесь
        tmp_fit = (eptemp_1 * norm.pdf(gridi, loc=emtemp_1, scale=estdtemp_1) +
                   eptemp_2 * norm.pdf(gridi, loc=emtemp_2, scale=estdtemp_2))
        tmp_fit = tmp_fit * (np.sum(kernel_density) / np.sum(tmp_fit))
        plt.plot(gridi, tmp_fit, '--b', linewidth=1, label='Гауссовская смесь')

        # Чувствительность
        tmp_resp = (eptemp_1 * norm.pdf(gridi, loc=emtemp_1, scale=estdtemp_1) /
                    (eptemp_1 * norm.pdf(gridi, loc=emtemp_1, scale=estdtemp_1) +
                     eptemp_2 * norm.pdf(gridi, loc=emtemp_2, scale=estdtemp_2)))
        plt.plot(gridi, tmp_resp, '-g', linewidth=1, label='Чувствительность')
        plt.title('Плотность ядра, максимальное правдоподобие для Гауссовской смеси и чувствительность')
        plt.legend()

        plt.tight_layout()
        plt.show()

    return results


# Пример использования (аналог Practice_07032025.m)
if __name__ == "__main__":
    # Параметры распределений
    mtemp_1 = 3  # среднее первого распределения
    mtemp_2 = 0.9  # среднее второго распределения
    stdtemp_1 = 0.9  # стандартное отклонение первого
    stdtemp_2 = 0.1  # стандартное отклонение второго
    Nobs = 200  # количество наблюдений
    Nmax = 300  # максимальное число итераций
    ptemp_1 = 0.2  # вероятность первого режима
    ptemp_2 = 0.8  # вероятность второго режима

    # Генерация данных
    np.random.seed(42)
    ytemp_1 = mtemp_1 + stdtemp_1 * np.random.randn(int(ptemp_1 * Nmax))
    ytemp_2 = mtemp_2 + stdtemp_2 * np.random.randn(int(ptemp_2 * Nmax))
    dat = np.concatenate([ytemp_1, ytemp_2])
    dat = dat[np.random.permutation(len(dat))[:Nobs]]  # случайная выборка

    tolerance = 1e-6

    # Начальные оценки
    m1 = np.mean(dat)
    m2 = np.mean(dat)
    std1_1 = np.std(dat) - np.std(dat) / 4
    std2_1 = np.std(dat)
    pi1_1 = 0.5
    pi2_1 = 1 - pi1_1

    # Запуск EM-алгоритма
    results = EM_normix(dat, Nmax, tolerance, plotflag=True)
    results['data'] = dat
    results['coef_true'] = [mtemp_1, mtemp_2, stdtemp_1, stdtemp_2, ptemp_1, ptemp_2]
    results['coef_est'] = [m1, m2, std1_1, std2_1, pi1_1, pi2_1]

    print('Фактические коэффициенты   Оценки коэффициентов')
    print(np.column_stack([results['coef_true'], results['coef_est']]))
    print(results['stopreason'])