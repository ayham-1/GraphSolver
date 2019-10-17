class Linear:

    def __init__(self, a, c, length):
        self.a = a
        self.c = c
        self.length = length

    def calc_linear_line(self):
        print([(0 - self.length, self.a * (0 - self.length)), (0 - self.length, self.a * self.length)])
