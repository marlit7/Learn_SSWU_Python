"""
Група вимог 2
розрахунок площі декількох фігур
"""

class Shape:
    def name(self):
        return "Фігура"
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def name(self):
        return "прямокутника"

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def name(self):
        return "кола"

    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def name(self):
        return "трикутника"

    def area(self):
        return self.base*self.height/2


if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(8),
        Triangle(5,9)

    ]

    for s in shapes:
        print(f"Площа {s.name()}:{s.area()}")