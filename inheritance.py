class Rectangle:

    def __init__(self, base, height):
        self._base = base
        self._height = height

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        self._base = base

    def area(self):
        return self._base * self._height

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
    
    @property
    def side(self):
        return self._base
    
    @side.setter
    def side(self, side):
        self._base = side
        self._height = side

def run():
    rectangle = Rectangle(3, 4)
    square = Square(4)
    print(rectangle.area())
    print(square.area())

if __name__ == '__main__':
    run()