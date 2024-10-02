import tkinter as tk
from PIL import ImageTk, Image
from scheme_element import SchemeElement


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.canvas_list = []
        self.button_list = []
        self.element_list = []

        new_canvas = tk.Canvas(self, width=250, height=130)
        new_canvas.grid(row=0, column=0)
        self.canvas_list.append(new_canvas)
        # self.img = ImageTk.PhotoImage(Image.open("schemes/scheme_1.png"))
        # canvas.create_image(5, 5, anchor="nw", image=self.img)
        new_button = tk.Button(self, anchor="nw", text="Запустить расчет")
        new_button.grid(row=2, column=0)
        self.button_list.append(new_button)
        new_button = tk.Button(self, anchor="nw", text="Сохранить")
        new_button.grid(row=2, column=1)
        self.button_list.append(new_button)
        new_button = tk.Button(self, anchor="nw", text="Загрузить")
        new_button.grid(row=2, column=2)
        self.button_list.append(new_button)
        new_button = tk.Button(self, text="Добавить", anchor="nw", command=self.add_scheme_element)
        new_button.grid(row=1, column=0)
        self.button_list.append(new_button)

    def add_scheme_element(self):
        choose_element_window = ChooseSchemeElementWindow()

        new_element_type = choose_element_window.chosen_type
        print(new_element_type)


class ChooseSchemeElementWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_list = []
        self.canvas_list = []
        self.button_list = []
        self.command_list = [self.choose_type_1, self.choose_type_2, self.choose_type_3, self.choose_type_4,
                             self.choose_type_5, self.choose_type_6, self.choose_type_7, self.choose_type_8]

        self.chosen_type = 1

        for i in range(0, 8):
            self.image_list.append(ImageTk.PhotoImage(Image.open(f"schemes/scheme_{i + 1}.png")))
            new_canvas = tk.Canvas(self, width=250, height=130)
            new_canvas.grid(row=i % 4, column=i // 4)
            self.canvas_list.append(new_canvas)
            new_button = tk.Button(self, text=f"Выбрать элемент {i + 1}", command=self.command_list[i])
            new_button.grid(row=i % 4, column=i // 4)
            self.button_list.append(new_button)

    def choose_type_1(self):
        print("type 1")
        self.chosen_type = 1
        self.destroy()

    def choose_type_2(self):
        print("type 2")
        self.chosen_type = 2
        self.destroy()

    def choose_type_3(self):
        print("type 3")
        self.chosen_type = 3
        self.destroy()

    def choose_type_4(self):
        print("type 4")
        self.chosen_type = 4
        self.destroy()

    def choose_type_5(self):
        print("type 5")
        self.chosen_type = 5
        self.destroy()

    def choose_type_6(self):
        print("type 6")
        self.chosen_type = 6
        self.destroy()

    def choose_type_7(self):
        print("type 7")
        self.chosen_type = 7
        self.destroy()

    def choose_type_8(self):
        print("type 8")
        self.chosen_type = 8
        self.destroy()


m = MainWindow()
tk.mainloop()
