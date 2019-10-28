class Linear:

    def __init__(self, a, c, length):
        self.a = a
        self.c = c
        self.length = length

    def calc_linear_line(self):
        print([(0 - self.length, self.a * (0 - self.length)), (0 - self.length, self.a * self.length)])

    def calc_intercept(self, x, y):

    	y1 = (x + y) / 3
    	y2 = ((3 * x) - (2 * y1)) / 4

        return y2

