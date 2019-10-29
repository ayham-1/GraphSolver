import math

class Linear:

    def __init__(self, a, c):
        # Line eq: y = ax + c
        self.a = a
        self.c = c

    def calcLinearIntersection(self, line):
        """
        This function accepts two lines of Linear class
        and returns the coordinates of intersection between the two lines

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