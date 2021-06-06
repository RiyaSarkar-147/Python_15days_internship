# Write a program with use of inheritance: Define a class publisher that stores the name of the title. Derive two classes book and tape, which inherit publisher. Book class contains member data called page no and tape class contain time for playing. Define functions in the appropriate classes to get and print the details.

class publisher():
    def __init__(self, title):
        self.title = title

    def gettitle(self):
        return self.title


class book(publisher):
    def __init__(self, title, pno):
        publisher.__init__(self, title)
        self.pno = pno

    def getpno(self):
        return self.pno


class tape(book):
    def __init__(self, title, pno, time):
        book.__init__(self, title, pno)
        self.time = time

    def gettime(self):
        return self.time


title = input("Enter the name of title: ")
pno = int(input("Enter Page Number: "))
time = (input("Enter Time: "))
obj = tape(title, pno, time)
print("Title Name: ", obj.gettitle())
print("Page Number: ", obj.getpno())
print("Time: ", obj.gettime())
