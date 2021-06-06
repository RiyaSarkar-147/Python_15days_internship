# Create a class cal4 that will calculate square of a number.
# Create setdata() method which has one parameters that contain number.
# Create display() method that will calculate sum.(Function should return value)
class cal4():
    def setdata(self, n):
        self.n = n

    def display(self):
        return(self.n**2)


obj = cal4()
obj.setdata(int(input("Enter the number: ")))
print("Square of number is:", obj.display())
