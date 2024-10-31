from math import exp


class Distribution:
    def __init__(self, distribution_type: str):
        self.valid_distribution_types = ['Экспоненциальное', 'Нормальное',
                                         'Вейбулла-Гнеденко', 'Рэлея']

        if distribution_type in self.valid_distribution_types:
            self.type = distribution_type
            self.params = {}
            self.set_default_params()
        else:
            ...

    def get_type(self):
        return self.type

    def get_params(self):
        return self.params

    def change_distribution_type(self, new_type: str):
        if new_type in self.valid_distribution_types:
            self.type = new_type
            self.params = {}
            self.set_default_params()
        else:
            ...

    def set_default_params(self):
        if self.type == 'Экспоненциальное':
            self.params['lambda'] = 0.015
        elif self.type == 'Нормальное':
            self.params['mu'] = 0.01
            self.params['sigma'] = 0.015
        elif self.type == 'Вейбулла-Гнеденко':
            self.params['lambda'] = 0.015
            self.params['alpha'] = 0.01
        else:
            self.params['alpha'] = 0.015

    def change_params(self, params: list[float]):
        if self.type == 'Экспоненциальное':
            self.params['lambda'] = 0
        elif self.type == 'Нормальное':
            self.params['mu'] = 0
            self.params['sigma'] = 0
        elif self.type == 'Вейбулла-Гнеденко':
            self.params['lambda'] = 0
            self.params['alpha'] = 0
        else:
            self.params['alpha'] = 0.015

        i = 0
        for key in self.params.keys():
            self.params[key] = params[i]
            i += 1

    def calc_probability(self, t: int):
        if self.type == 'Экспоненциальное':
            return exp(-self.params['lambda'] * t)
        elif self.type == 'Нормальное':
            ...
        elif self.type == 'Вейбулла-Гнеденко':
            return exp(-self.params['lambda'] * t ** (self.params['alpha']))
        else:
            if t <= 0:
                return 0
            else:
                return exp(-t ** 2 / (2 * self.params['alpha'] ** 2))
