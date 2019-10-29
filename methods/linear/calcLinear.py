import math


class Linear:

    def __init__(self, a, c, length):
        self.a = a
        self.c = c
        self.length = length

    def calc_linear_line(self):
        print([(0 - self.length, self.a * (0 - self.length)),
               (0 - self.length, self.a * self.length)])

    def calcLinearIntersection(self, line):
        """
        This function accepts one line of Linear class
        and returns the coordinates of intersection
        between the self and the line passed

        If there is no intercept it returns 0
        If there are infinite intercepts it return math.inf
        If there is one unique intercept it returns a tuple with (x, y)
        """

        if self.a == line.a:
            if self.c == line.c:
                return math.inf
            return 0

        x = (line.c-self.c)/(self.a - line.a)
        y = self.a*(line.c - self.c)/(self.a - line.a) + self.c

        return (x, y)
