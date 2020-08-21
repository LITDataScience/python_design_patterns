# LSP
class Rectangle:
    def __init__(self, height, width):
        # Keeping them private to create a property out of them
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # To make sure a Square remains a square (with all the dimensions equal)
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10 # For the Square() this line will break the LSP. Hence, I would prefer using a factory method for Square()
    expected = int(w * 10)
    print(f'Expected an area of {expected}, instead got an area of {rc.area}')


rc = Rectangle(3, 2)
use_it(rc)

sq = Square(5)
use_it(sq)
