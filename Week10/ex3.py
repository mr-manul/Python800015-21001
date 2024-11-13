class Point:
    def __init__(this, x, y):
        this.x = x
        this.y = y

    def __str__(this):
        return f'({this.x}, {this.y})'

    def __add__(this, other):
        if isinstance(other, Point):
            return Point(this.x + other.x, this.y + other.y)
        return NotImplemented

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)

