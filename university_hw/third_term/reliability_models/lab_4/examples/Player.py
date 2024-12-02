from app.asm2304.st04.IOStrategy import WebIO


class Player:
    def __init__(self):
        self.name = ""
        self.number = 0

        self.io = WebIO

    def read(self):
        self.name = self.io.input('name')
        self.number = self.io.input('number')

    def write(self):
        self.io.output(self.name)
        self.io.output(self.number)
