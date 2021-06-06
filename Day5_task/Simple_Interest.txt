# Create a class cal3 that will calculate simple interest.
# Create constructor method which has three parameters .
# Create calInterest() method that will calculate Interest .
# Create display() method that will display Interest.
class cal3:

    def __init__(self, p, r, n):
        self.p = p
        self.r = r
        self.n = n

    def calInterest(self):
        return((self.p*self.r*self.n)/100)

    def display(self):
        return(self.calInterest())


p = float(input("Enter Principle Amount: "))
r = float(input("Enter rate of interst: "))
n = int(input("Enter the number of months: "))
obj = cal3(p, r, n)
print("Simple Interest is:", obj.display())
