class Rectangle:

    def __init__(self, length, width):
        try:
            self._length = int(length)
            self._width = int(width)

        except:
            raise ValueError()

        if length < 0 or width < 0:
            raise ValueError()

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def calculate_squre(self):
        return self._length*self._width

    def calculate_perimeter(self):
        return (self._length+self._width) * 2

rectangle = Rectangle(5, 7)

print(rectangle.calculate_perimeter())
print(rectangle.calculate_squre())
print(rectangle.width)
print(rectangle.length)

