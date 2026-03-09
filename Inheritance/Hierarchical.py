'''
Hierarchical Inheritence
'''


class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def draw_circle(self):
        print("Drawing circle")

class Square(Shape):
    def draw_square(self):
        print("Drawing square")

c = Circle()
s = Square()

c.display()
c.draw_circle()

s.display()
s.draw_square()