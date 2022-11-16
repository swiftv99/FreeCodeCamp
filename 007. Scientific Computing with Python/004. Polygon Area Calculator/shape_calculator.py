class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = (("*" * self.width) + '\n') * self.height
        return picture

    def get_amount_inside(self, obj):
        return self.get_area() // obj.get_area()


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side


""" Alternative
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
      return f'Square(side={self.width})'

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
"""


# rect = Rectangle(7, 5)
# print(rect)
# print(rect.get_picture())
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())
# rect = Rectangle(8, 16)
# rect2 = Rectangle(2, 4)
# sq = Square(4)
# print(rect.get_area(), sq.get_area())
# print(rect.get_amount_inside(sq))
# print(rect.get_amount_inside(rect2))
