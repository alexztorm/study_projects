from app.asm2304.st04.Player import Player


class Goalkeeper(Player):
    def __init__(self):
        super().__init__()
        self.position = "goalkeeper"
        self.saves = 0

    def read(self):
        super().read()
        self.saves = self.io.input('saves')

    def write(self):
        super().write()
        self.io.output(self.position)
        self.io.output(self.saves)
