import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
        self.buttons = []
        self.labels = []

        self.setup_labels()
        self.setup_buttons()

    def setup_labels(self):
        names = ['Моменты времени', 'Работающие объекты', 'Отказавшие объекты', 'Вероятность отказа']

        for i in range(len(names)):
            new_label = tk.Label(self, text=names[i])
            new_label.grid(row=0, column=i)
            self.labels.append(new_label)

    def setup_buttons(self):
        add_button = tk.Button(self, text='Добавить', command=self.add_line)
        add_button.grid(row=1, column=0)
        self.buttons.append(add_button)

    def add_line(self):
        ...

    def show_results(self):
        result_window = ResultWindow(self.data)
        self.wait_window(result_window)


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
