from app.asm2304.st04.Player import Player


class Forward(Player):
    def __init__(self):
        super().__init__()
        self.position = "forward"
        self.goals = 0

    def read(self):
        super().read()
        self.goals = self.io.input('goals')

    def write(self):
        super().write()
        self.io.output(self.position)
        self.io.output(self.goals)
