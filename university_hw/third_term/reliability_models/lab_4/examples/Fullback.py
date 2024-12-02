from app.asm2304.st04.Player import Player


class FullBack(Player):
    def __init__(self):
        super().__init__()
        self.position = "fullback"
        self.counters = 0

    def read(self):
        super().read()
        self.counters = self.io.input('counters')

    def write(self):
        super().write()
        self.io.output(self.position)
        self.io.output(self.counters)
