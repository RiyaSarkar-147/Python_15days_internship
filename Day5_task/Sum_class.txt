# Create a class cal1 that will calculate sum of three numbers.
# Create setdata() method which has three parameters that contain numbers.
# Create display() method that will calculate sum and display sum.
class cal1:
    def setdata(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        return(self.a+self.b+self.c)


obj = cal1()
obj.setdata(10, 20, 30)
print("Summation is:", obj.display())
