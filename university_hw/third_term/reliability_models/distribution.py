from math import exp


class Distribution:
    def __init__(self, distribution_type: str):
        self.valid_distribution_types = ['Экспоненциальное', 'Нормальное',
                                         'Вейбулла-Гнеденко', 'Рэлея']

        if distribution_type in self.valid_distribution_types:
            self.type = distribution_type
            self.params = {}
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
        else:
            ...

    def change_params(self, params: list[float]):
        if self.type == 'Экспоненциальное':
            self.params['lambda'] = 0
        elif self.type == 'Нормальное':
            ...
        elif self.type == 'Вейбулла-Гнеденко':
            self.params['lambda'] = 0
            self.params['mu'] = 0
        else:
            ...

        i = 0
        for key in self.params.keys():
            self.params[key] = params[i]
            i += 1

    def calc_probability(self, t: int):
        if self.type == 'Экспоненциальное':
            return exp(- self.params['lambda'] * t)
        elif self.type == 'Нормальное':
            ...
        elif self.type == 'Вейбулла-Гнеденко':
            return (exp(- self.params['lambda'] / self.params['mu'])
                    * (1 - exp(- self.params['lambda'] / self.params['mu'])))
        else:
            ...
