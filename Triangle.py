def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (a != 0) and (b != 0 ) and (c != 0):
        if (a + b) >= c and (a + c) >= b and (b + c) >= a:
            if a == b == c:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a != 0) and (b != 0 ) and (c != 0):
        if (a + b) >= c and (a + c) >= b and (b + c) >= a:
            if (a == b) or (a == c) or (b == c):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a != 0) and (b != 0 ) and (c != 0):
        if (a + b) >= c and (a + c) >= b and (b + c) >= a:
            if (a != b) and (a != c) and (b != c):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
