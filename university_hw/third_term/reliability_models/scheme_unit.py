from PIL import ImageTk, Image
from distribution import Distribution


class SchemeUnit:
    def __init__(self, type_of_scheme: int, start_time: int = 0):
        self.start_time = start_time

        self.image = None
        self.number_of_blocks = 0
        self.distribution = []
        self.times = []
        self.probability = 1

        self.change_unit_type(type_of_scheme)
    
    def change_distribution(self, distribution):
        self.distribution = distribution

    def change_unit_type(self, new_type):
        if new_type == 1:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_1.png"))
            self.number_of_blocks = 1
        elif new_type == 2:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_2.png"))
            self.number_of_blocks = 2
        elif new_type == 3:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_3.png"))
            self.number_of_blocks = 3
        elif new_type == 4:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_4.png"))
            self.number_of_blocks = 4
        elif new_type == 5:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_5.png"))
            self.number_of_blocks = 3
        elif new_type == 6:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_6.png"))
            self.number_of_blocks = 4
        elif new_type == 7:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_7.png"))
            self.number_of_blocks = 5
        elif new_type == 8:
            self.image = ImageTk.PhotoImage(Image.open("schemes/scheme_8.png"))
            self.number_of_blocks = 6

        self.times = [0] * self.number_of_blocks

        for i in range(self.number_of_blocks):
            self.distribution.append(Distribution('Экспоненциальное'))

    def edit_block_distribution(self, block_num, new_distribution):
        self.distribution[block_num].change_distribution_type(new_distribution)

    def edit_block_time(self, block_num, new_time):
        self.times[block_num] = new_time

    def calc_probability(self, unit_type):
        ...
