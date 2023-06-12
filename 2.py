class Rectangle(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

# rect = Rectangle(4,4,4,4)
# print(rect.get_perimeter())
