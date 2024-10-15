from PIL import ImageTk, Image


class SchemeUnit:
    def __init__(self, type_of_scheme, start_time=0):
        self.start_time = start_time

        self.image = None
        self.number_of_blocks = 0
        self.distribution = "exponential"
        self.probability = None

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
