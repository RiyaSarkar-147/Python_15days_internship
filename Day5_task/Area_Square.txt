# Create a class cal6 that will calculate area of a square.
# Create setdata() method that should take length from the user.
# Create area() method that will calculate area .
# Create display() method that will display area .
class cal6():
    def setdata(self, a):
        self.a = a

    def area(self):
        return(self.a*self.a)

    def display(self):
        return(self.area())


obj = cal6()
obj.setdata(int(input("Enter the side length : ")))
print("Area of square is:", obj.display())
