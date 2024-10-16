import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

from scheme_unit import SchemeUnit
from storage import DBStorage, FileStorage


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_list = []
        self.button_list = []
        self.unit_list = []
        self.max_unit_number = 8

        self.introduction_label = tk.Label(self, text='Добавьте элемент')
        self.introduction_label.grid(row=0, column=0, columnspan=2)

        self.time_period_label = tk.Label(self, text='Укажите время расчета в месяцах:')
        self.time_period_label.grid(row=2, column=0, columnspan=2)

        self.time_period_entry = tk.Entry(self)
        self.time_period_entry.grid(row=2, column=2, columnspan=2)

        self.probability_label = tk.Label(self, text='Укажите P критическое:')
        self.probability_label.grid(row=3, column=0, columnspan=2)

        self.probability_entry = tk.Entry(self)
        self.probability_entry.grid(row=3, column=2, columnspan=2)

        new_button = tk.Button(self, anchor="nw", text="Запустить расчет", command=self.start_calc)
        new_button.grid(row=5, column=0, columnspan=2)
        self.button_list.append(new_button)
        new_button = tk.Button(self, anchor="nw", text="Сохранить")
        new_button.grid(row=5, column=2)
        self.button_list.append(new_button)
        new_button = tk.Button(self, anchor="nw", text="Загрузить")
        new_button.grid(row=5, column=3)
        self.button_list.append(new_button)
        new_button = tk.Button(self, text="Добавить", anchor="nw", command=self.add_scheme_unit)
        new_button.grid(row=4, column=0, columnspan=2)
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
        new_label = tk.Label(self, image=unit.image)
        new_label.grid(row=1, column=2 * len(self.label_list), columnspan=2, pady=5)
        new_label.bind('<Button-1>', lambda event, unit_id=len(self.label_list): self.edit_unit(event, unit_id))
        new_label.bind('<Button-3>', lambda event, unit_id=len(self.label_list): self.delete_unit(event, unit_id))

        self.label_list.append(new_label)
        self.introduction_label['text'] = 'LMB - редактировать, RMB - удалить'

    def delete_unit(self, event, unit_id):
        tmp = self.label_list.pop(unit_id)
        tmp.destroy()
        if not self.label_list:
            self.introduction_label['text'] = 'Добавьте элемент'
        self.update_labels()
        self.unit_list.pop(unit_id)

    def edit_unit(self, event, unit_id):
        edit_window = EditUnitWindow(self.unit_list[unit_id])
        self.wait_window(edit_window)

    def update_labels(self):
        for i in range(len(self.label_list)):
            self.label_list[i].grid(row=1, column=2 * i, columnspan=2, pady=5)
            self.label_list[i].bind('<Button-1>', lambda event, unit_id=i: self.edit_unit(event, unit_id))
            self.label_list[i].bind('<Button-3>', lambda event, unit_id=i: self.delete_unit(event, unit_id))

    def start_calc(self):
        try:
            time, critical_probability = int(self.time_period_entry.get()), float(self.probability_entry.get())

            if not self.check_correct_entry_filling(time, critical_probability):
                messagebox.showerror("Ошибка", "Ошибка ввода данных!")
            else:
                ...
        except ValueError:
            messagebox.showerror("Ошибка", "Ошибка ввода данных!")

    @staticmethod
    def check_correct_entry_filling(time_entry_value: int, probability_entry_value: float) -> bool:
        if not time_entry_value or not probability_entry_value:
            return False
        if time_entry_value <= 0:
            return False
        if 0 >= probability_entry_value or probability_entry_value >= 1:
            return False
        return True


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


class EditUnitWindow(tk.Toplevel):
    def __init__(self, unit: SchemeUnit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unit = unit

        self.image_label = tk.Label(self, image=self.unit.image)
        self.image_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self.distribution_label = tk.Label(self, text='Выбрать распределения: ')
        self.distribution_label.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.combobox_list = []
        self.combobox_values = ['Экспоненциальное', 'Нормальное', 'Вейбулла-Гнеденко', 'Рэлея']
        self.combobox_vars = []

        for i in range(self.unit.number_of_blocks):
            block_label = tk.Label(self, text=f'Элемент {i + 1}:')
            block_label.grid(row=i + 2, column=0, padx=5, pady=5)
            new_var = tk.StringVar(value=self.unit.distribution[i])
            self.combobox_vars.append(new_var)
            new_combobox = ttk.Combobox(self, textvariable=new_var, values=self.combobox_values, state='readonly')
            new_combobox.grid(row=i + 2, column=1, padx=5, pady=5)
            self.combobox_list.append(new_combobox)

        self.accept_button = tk.Button(self, text='Подтвердить', command=self.accept_changes)
        self.accept_button.grid(row=2 + self.unit.number_of_blocks, column=0, padx=5, pady=5, columnspan=2)

    def accept_changes(self):
        for i in range(self.unit.number_of_blocks):
            self.unit.distribution[i] = self.combobox_list[i].get()
        self.destroy()


m = MainWindow()
tk.mainloop()
