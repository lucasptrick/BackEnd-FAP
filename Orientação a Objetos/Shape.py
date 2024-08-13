class Shape:
    def __init__(self, sideOne, sideTwo):
        self.sideOne = sideOne
        self.sideTwo = sideTwo

    def getArea(self):
        return self.sideTwo * self.sideTwo

    def __str__(self) -> str:
        return f'The area of this {self.__class__.__name__} is: {self.getArea}'


class Rectangle(Shape):
    def __init__(self, base, altura):
        super().__init__(base, altura)


class Square(Rectangle):
    def __init__(self, lado):
        super().__init__(lado, lado)


class Triangle(Rectangle):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def getArea(self):
        a = super().getArea()
        return a / 2

from math import pi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return f"{(pi * (self.radius ** 2)):.2f}"


rec = Rectangle(3,3)
sqr = Square(2)
tri = Triangle(4,6)
cir = Circle(2)

print(rec.getArea())
print('\n')
print(sqr.getArea())
print('\n')
print(tri.getArea())
print('\n')
print(cir.getArea())
print('\n')


