import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.canvas_list = []
        self.button_list = []

        new_canvas = tk.Canvas(self, width=250, height=130)
        new_canvas.grid(row=0, column=0)
        self.canvas_list.append(new_canvas)
        # self.img = ImageTk.PhotoImage(Image.open("schemes/scheme_1.png"))
        # canvas.create_image(5, 5, anchor="nw", image=self.img)
        new_button = tk.Button(self, text="Запустить расчет")
        new_button.grid(row=2, column=0)
        self.button_list.append(new_button)
        new_button = tk.Button(self, text="Добавить", command=self.add_scheme_element)
        new_button.grid(row=1, column=0)
        self.button_list.append(new_button)

    def add_scheme_element(self):
        ...


m = MainWindow()
tk.mainloop()
