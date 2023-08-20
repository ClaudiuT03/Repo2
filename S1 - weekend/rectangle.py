
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length= length

    def get_area(self):
       aria =self.length * self.width
       print(aria)

my_obj = Rectangle(2,6)

my_obj.get_area()