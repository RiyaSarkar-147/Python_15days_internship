# Create a class cal5 that will calculate area of a rectangle.
# Create constructor method which has two parameters .
# Create calArea() method that will calculate area of a rectangle.
# Create display() method that will display area of a rectangle.
class cal5:

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calArea(self):
        return((self.l*self.w))

    def display(self):
        return(self.calArea())


l = float(input("Enter length: "))
w = float(input("Enter width: "))
obj = cal5(l, w)
print("Area of Rectangle is:", obj.display())
