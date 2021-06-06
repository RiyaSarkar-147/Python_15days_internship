# Create a class cal2 that will calculate area of a circle.
# Create setdata() method that should take radius from the user.
# Create area() method that will calculate area .
# Create display() method that will display area .
class cal2:
    def setdata(self, r):
        self.r = r

    def display(self):
        return(3.14*self.r*self.r)


obj = cal2()
obj.setdata(float(input("Enter the radius of the circle: ")))
print("Area of the circle is:", obj.display())
