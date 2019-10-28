import math

def calcLinearIntersection(line1, line2):
    """
    This function accepts two lines of Linear class
    and returns the coordinates of intersection between the two lines

    If there is no intercept it returns 0
    If there are infinite intercepts it return math.inf
    If there is one unique intercept it returns a tuple with (x, y)
    """

    if line1.a == line2.a:
        if line1.c == line2.c:
            return math.inf
        return 0

    x = (line2.c-line1.c)/(line1.a - line2.a)
    y = line1.a*(line2.c - line1.c)/(line1.a - line2.a) + line1.c

    return (x, y)
