import os


class Holsted:
    def __init__(self):
        with open('operators.txt', 'r') as file_operators:
            self.operators = set(file_operators.read().split('\n'))

    def analyze(self):
        ...

    def calc_holsted(self):
        ...

    @staticmethod
    def show_examples():
        files = os.listdir('./examples')

        for file in files:
            print(file)


h = Holsted()
h.show_examples()
