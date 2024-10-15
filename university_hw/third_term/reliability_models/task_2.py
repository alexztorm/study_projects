import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from scheme_unit import SchemeUnit


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_list = []
        self.button_list = []
        self.unit_list = []
        self.max_unit_number = 8

        new_label = tk.Label(self, text='Добавьте первый элемент')
        new_label.grid(row=0, column=0, columnspan=2, pady=5)
        self.label_list.append(new_label)
        new_button = tk.Button(self, anchor="nw", text="Запустить расчет")
        new_button.grid(row=3, column=0)
        self.button_list.append(new_button)
        new_button = tk.Button(self, anchor="nw", text="Сохранить")
        new_button.grid(row=3, column=1)
        self.button_list.append(new_button)
        new_button = tk.Button(self, anchor="nw", text="Загрузить")
        new_button.grid(row=3, column=2)
        self.button_list.append(new_button)
        new_button = tk.Button(self, text="Добавить", anchor="nw", command=self.add_scheme_unit)
        new_button.grid(row=2, column=0)
        self.button_list.append(new_button)

    def add_scheme_unit(self):
        if len(self.label_list) < self.max_unit_number:
            choose_unit_window = ChooseSchemeUnitWindow()
            self.wait_window(choose_unit_window)

            new_unit_type = choose_unit_window.chosen_type
            new_unit = SchemeUnit(new_unit_type)

            self.draw_unit(new_unit)
            self.unit_list.append(new_unit)
        else:
            messagebox.showerror("Ошибка", "Достигнут лимит элементов цепи")

    def draw_unit(self, unit: SchemeUnit):
        if len(self.label_list) == 1 and self.label_list[0]['text'] == 'Добавьте первый элемент':
            tmp = self.label_list.pop()
            tmp.destroy()
        new_label = tk.Label(self, image=unit.image)
        new_label.grid(row=0, column=2 * len(self.label_list), columnspan=2, pady=5)
        new_label.bind('<Button-1>', lambda event, unit_id=len(self.label_list): self.edit_unit(event, unit_id))
        new_label.bind('<Button-3>', lambda event, unit_id=len(self.label_list): self.delete_unit(event, unit_id))

        self.label_list.append(new_label)

    def delete_unit(self, event, unit_id):
        tmp = self.label_list.pop(unit_id)
        tmp.destroy()
        self.update_labels()
        self.unit_list.pop(unit_id)

    def edit_unit(self, event, unit_id):
        print('edit', unit_id)

    def update_labels(self):
        for i in range(len(self.label_list)):
            self.label_list[i].grid(row=0, column=2 * i, columnspan=2, pady=5)
            self.label_list[i].bind('<Button-1>', lambda event, unit_id=i: self.edit_unit(event, unit_id))
            self.label_list[i].bind('<Button-3>', lambda event, unit_id=i: self.delete_unit(event, unit_id))


class ChooseSchemeUnitWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_list = []
        self.label_list = []
        self.button_list = []
        self.command_list = [self.choose_type_1, self.choose_type_2, self.choose_type_3, self.choose_type_4,
                             self.choose_type_5, self.choose_type_6, self.choose_type_7, self.choose_type_8]

        self.chosen_type = 1

        for i in range(0, 8):
            self.image_list.append(ImageTk.PhotoImage(Image.open(f"schemes/scheme_{i + 1}.png")))
            new_label = tk.Label(self, image=self.image_list[i])
            new_label.grid(row=2 * (i % 4), column=i // 4, padx=5, pady=5)
            self.label_list.append(new_label)
            new_button = tk.Button(self, text=f"Выбрать элемент {i + 1}", command=self.command_list[i])
            new_button.grid(row=2 * (i % 4) + 1, column=i // 4, padx=5, pady=5)
            self.button_list.append(new_button)

    def choose_type_1(self):
        self.chosen_type = 1
        self.destroy()

    def choose_type_2(self):
        self.chosen_type = 2
        self.destroy()

    def choose_type_3(self):
        self.chosen_type = 3
        self.destroy()

    def choose_type_4(self):
        self.chosen_type = 4
        self.destroy()

    def choose_type_5(self):
        self.chosen_type = 5
        self.destroy()

    def choose_type_6(self):
        self.chosen_type = 6
        self.destroy()

    def choose_type_7(self):
        self.chosen_type = 7
        self.destroy()

    def choose_type_8(self):
        self.chosen_type = 8
        self.destroy()


m = MainWindow()
tk.mainloop()
