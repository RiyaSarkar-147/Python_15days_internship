# Create a arith class. The class should have a parameterized constructor and methods to add, subtract and multiply two numbers and to return the answers.

class arith():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return(self.a+self.b)

    def subtract(self):
        return(self.a-self.b)

    def multiply(self):
        return(self.a*self.b)


a = int(input("Enter first integer number: "))
b = int(input("Enter secind integer number: "))
obj = arith(a, b)
print("Summation is: ", obj.add())
print("Subtraction is: ", obj.subtract())
print("Multiplication is: ", obj.multiply())
