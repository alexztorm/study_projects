from os import listdir
from math import log2


class HolstedsMetric:
    def __init__(self):
        with open('operators.txt', 'r') as operators_list:
            self.operators_dict = operators_list.read().split('\n')

        self.operators = []
        self.operands = []

        self.result = []
        self.file_names = []

    def start(self):
        files = self.read_examples()

        for file in files:
            with open('./examples/' + file, 'r') as read_file:
                code = read_file.read()
                self.count_operators_and_operands(code)
                self.form_result()
                self.file_names.append(file)

                self.operators = []
                self.operands = []

        self.output()

    def count_operators_and_operands(self, code):
        contents = []

        for line in code.split('\n'):
            if line:
                contents.append(line.split())

        for line in contents:
            for element in line:
                if element in self.operators_dict:
                    self.operators.append(element)
                else:
                    if element.isdigit():
                        self.operands.append(element)
                    else:
                        if not self.check_for_dot(element):
                            if not self.check_for_brackets(element):
                                if not self.check_for_equality(element):
                                    if not self.check_for_double_dots(element):
                                        self.operands.append(element)

    def check_for_dot(self, element):
        if '.' in element:
            element_combination = element.split('.')

            for el in element_combination:
                if el in self.operators_dict:
                    self.operators.append(el)
                else:
                    if not self.check_for_brackets(el):
                        if not self.check_for_equality(el):
                            if not self.check_for_double_dots(el):
                                self.operands.append(el)
            return True
        else:
            return False

    def check_for_brackets(self, element):
        if '(' in element:
            element_combination = element.split('(')

            for el in element_combination:
                if ')' in el:
                    el = el.replace(')', '')
                if el in self.operators_dict:
                    self.operators.append(el)
                else:
                    if not self.check_for_equality(el):
                        if not self.check_for_double_dots(el):
                            self.operands.append(el)
            return True
        elif ')' in element:
            element = element.replace(')', '')
            if element in self.operators_dict:
                self.operators.append(element)
            else:
                if not self.check_for_equality(element):
                    if not self.check_for_double_dots(element):
                        self.operands.append(element)
            return True
        else:
            return False

    def check_for_equality(self, element):
        if '=' in element:
            self.operators.append('=')
            element_combination = element.split('=')

            for el in element_combination:
                if el in self.operators_dict:
                    self.operators.append(el)
                else:
                    if not self.check_for_double_dots(el):
                        self.operands.append(el)

            return True
        else:
            return False

    def check_for_double_dots(self, element):
        if ':' in element:
            element = element.replace(':', '')

            if element in self.operators_dict:
                self.operators.append(element)
            else:
                self.operands.append(element)

            return True
        else:
            return False

    @staticmethod
    def read_examples():
        files = listdir('./examples')
        return files

    def form_result(self):
        N1 = len(self.operators)            # общее число операторов в программе
        N2 = len(self.operands)             # общее число операндов в программе
        n1 = len(set(self.operators))       # число уникальных операторов программы
        n2 = len(set(self.operands))        # число уникальных операндов программы

        N = N1 + N2                         # длина программы
        n = n1 + n2                         # словарь программы
        Nt = n1 * log2(n1) + n2 * log2(n2)  # теоретическая длина программы

        V = N * log2(n)                     # объем программы
        Lt = (2 * n2) / (n1 * N2)           # уровень качества программирования
        Ec = V / Lt ** 2                    # сложность понимания программы
        D = 1 / Lt                          # трудоемкость кодирования программы
        yt = V / D ** 2                     # уровень языка выражения
        I = V / D                           # умственные затраты на создание программы

        metrics = {
            'n1': n1,
            'n2': n2,
            'N1': N1,
            'N2': N2,
            'n': n,
            'N': N,
            'N\'': Nt,
            'V': V,
            'L\'': Lt,
            'Ec': Ec,
            'D': D,
            'y\'': yt,
            'I': I
        }

        self.result.append(metrics)

    def output(self):
        for i in range(len(self.result)):
            print(f'{self.file_names[i]} - {self.result[i]}')


h = HolstedsMetric()
h.start()
