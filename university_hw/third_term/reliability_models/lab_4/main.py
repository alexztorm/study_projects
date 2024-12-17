import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from os import listdir

from holsted import HolstedsMetric
from chepin import ChepinMetric
from storage import DBStorage
from report_maker import ReportMaker


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.example_path = './examples'

        self.frame1, self.frame2 = tk.Frame(self, relief="flat"), tk.Frame(self)
        self.frame1.pack(padx=20, pady=20)
        self.frame2.pack(padx=20, pady=20)

        self.checkboxes = []
        self.checkbox_states = []
        self.buttons = []
        self.choose_metric = None

        self.setup_frame1()
        self.setup_frame2()

        self.holsted_calculator = HolstedsMetric()
        self.chepin_calculator = ChepinMetric()

        self.chosen_files = []

        self.experiment_num = 0

        self.db_storage = DBStorage()
        self.report_maker = ReportMaker()

    def setup_frame1(self):
        files = listdir(self.example_path)

        for file in files:
            new_var = tk.BooleanVar()
            new_checkbox = ttk.Checkbutton(self.frame1, text=file, variable=new_var)
            new_var.set(True)
            new_checkbox.pack(fill='both')
            self.checkboxes.append(new_checkbox)
            self.checkbox_states.append(new_var)

    def setup_frame2(self):
        button_choose = tk.Button(self.frame2, text='Выбрать', command=self.button_choose)
        button_choose.grid(row=0, column=0, sticky='nsew')
        self.buttons.append(button_choose)

        button_report = tk.Button(self.frame2, text='Сформировать отчет', command=self.button_report, state='disabled')
        button_report.grid(row=0, column=1, sticky='nsew')
        self.buttons.append(button_report)

        button_calc = tk.Button(self.frame2, text='Расчет', command=self.button_calc, state='disabled')
        button_calc.grid(row=1, column=1, sticky='nsew')
        self.buttons.append(button_calc)

        self.choose_metric = ttk.Combobox(self.frame2, state='readonly')
        self.choose_metric['values'] = ('Метрика Холстеда', 'Метрика Чепина')
        self.choose_metric.current(0)
        self.choose_metric.grid(row=1, column=0, sticky='nsew')

    def button_choose(self):
        self.chosen_files = []
        at_least_one_chosen = False

        for i in range(len(self.checkbox_states)):
            if self.checkbox_states[i].get() is True:
                self.chosen_files.append(self.checkboxes[i].cget('text'))
                at_least_one_chosen = True

        if not at_least_one_chosen:
            messagebox.showwarning("Внимание", "Выберите хотя бы один файл!")
            self.buttons[1]['state'] = 'disabled'
            self.buttons[2]['state'] = 'disabled'
        else:
            self.buttons[1]['state'] = 'normal'
            self.buttons[2]['state'] = 'normal'

    def button_calc(self):
        self.experiment_num += 1

        chosen_metric = self.choose_metric['values'][self.choose_metric.current()]

        if chosen_metric == 'Метрика Холстеда':
            self.holsted_calculator.set_data(self.chosen_files)
            res = self.holsted_calculator.start()

            self.db_storage.store_holsted(res, self.experiment_num, self.chosen_files)
        else:
            self.chepin_calculator.set_data(self.chosen_files)
            res = self.chepin_calculator.start()

            self.db_storage.store_chepin(res, self.experiment_num, self.chosen_files)

    def button_report(self):
        res1, res2 = self.db_storage.load()

        res = res1 + res2

        self.report_maker.make_report(res)


m = MainWindow()
m.mainloop()
