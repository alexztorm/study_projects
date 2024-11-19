import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from storage import DBStorage, FileStorage


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buttons = []
        self.labels = []
        self.entry_table = []

        self.db_storage = DBStorage()
        self.file_storage = FileStorage()

        self.setup_labels()
        self.setup_buttons()

    def setup_labels(self):
        names = ['Моменты времени (t_i)', 'Работающие объекты (R_i)', 'Отказавшие объекты (d_i)',
                 'Вероятность отказа (d_i/R_i)']

        for i in range(len(names)):
            new_label = tk.Label(self, text=names[i])
            new_label.grid(row=0, column=i)
            self.labels.append(new_label)

    def setup_buttons(self):
        add_button = tk.Button(self, text='Добавить', command=self.add_line)
        add_button.grid(row=1, column=0)
        self.buttons.append(add_button)

        names = ['Рассчитать', 'Сохранить в БД', 'Загрузить из БД', 'Сохранить в файл', 'Загрузить из файла']
        commands = [self.start_calc, self.db_store, self.db_load, self.file_store, self.file_load]

        for i in range(len(names)):
            new_button = tk.Button(self, text=names[i], command=commands[i])
            new_button.grid(row=2, column=i)
            self.buttons.append(new_button)

    def add_line(self):
        new_line = []

        for i in range(4):
            new_entry = tk.Entry(self)
            new_entry.bind('<FocusOut>',
                           lambda event, c=i, r=len(self.entry_table): self.update_line_on_leave(event, r, c))
            new_entry.bind('<Return>', self.update_line_on_return)
            new_entry.grid(row=len(self.entry_table)+1, column=i)
            new_line.append(new_entry)

        self.entry_table.append(new_line)
        self.move_buttons_down()

    def update_line_on_leave(self, event, row, column):
        if column == 1:
            R = self.entry_table[row][column].get()
            d = self.entry_table[row][2].get()
            dr = self.entry_table[row][3].get()
            if R and dr:
                self.entry_table[row][2].delete(0, 'end')
                self.entry_table[row][2].insert(0, f'{int(int(R) * float(dr))}')
            elif R and d and R != 0:
                self.entry_table[row][3].delete(0, 'end')
                self.entry_table[row][3].insert(0, f'{int(d) / int(R): .2f}')
        elif column == 2:
            R = self.entry_table[row][1].get()
            d = self.entry_table[row][column].get()
            if R and d and R != 0:
                self.entry_table[row][3].delete(0, 'end')
                self.entry_table[row][3].insert(0, f'{int(d) / int(R): .2f}')
        elif column == 3:
            R = self.entry_table[row][1].get()
            dr = self.entry_table[row][column].get()
            if R and dr:
                self.entry_table[row][2].delete(0, 'end')
                self.entry_table[row][2].insert(0, f'{int(int(R) * float(dr))}')

    def update_line_on_return(self, event):
        self.focus_set()

    def get_table_values(self):
        values = []
        for line in self.entry_table:
            new_line = []
            full_line_flag = True
            for i in range(len(line)):
                input_value = line[i].get()
                if input_value:
                    if i == 3:
                        new_line.append(float(line[i].get()))
                    else:
                        new_line.append(int(line[i].get()))
                else:
                    full_line_flag = False
                    break
            if full_line_flag:
                values.append(new_line)

        return values

    def start_calc(self):
        ...

    def db_store(self):
        self.db_storage.store(self.get_table_values())

    def db_load(self):
        values = self.db_storage.load()
        self.update_table(values)

    def file_store(self):
        self.file_storage.store(self.get_table_values())

    def file_load(self):
        values = self.file_storage.load()
        self.update_table(values)

    def update_table(self, new_values):
        ...

    def show_results(self):
        result_window = ResultWindow(self.get_table_values())
        self.wait_window(result_window)

    def move_buttons_down(self):
        for button in self.buttons:
            pos = button.grid_info()
            button.grid(row=pos['row'] + 1, column=pos['column'])


class ResultWindow(tk.Toplevel):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Результаты')
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(data)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()


main_window = MainWindow()
main_window.mainloop()
