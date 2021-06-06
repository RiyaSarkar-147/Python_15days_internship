# Consider an employee class, which contains fields such as name and designation.
# And a subclass, which contains a field salary.
# Write a program for inheriting this relation.
class employee():
    def __init__(self, name, des):
        self.name = name
        self.des = des

    def getname(self):
        return self.name

    def getdes(self):
        return self.des


class salary(employee):
    def __init__(self, name, des, sal):
        employee.__init__(self, name, des)
        self.sal = sal

    def getsal(self):
        return self.sal


name = input("Enter name: ")
des = input("Enter designation: ")
sal = int(input("Enter Salary: "))
obj = salary(name, des, sal)
print(obj.getname()+" "+obj.getdes()+" "+obj.getsal())
