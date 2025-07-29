class Person():
    CityName="mumbai"

    def printName(self,name):
        print(name)

class ECStudent1(Person):
    def printDeatlis(self):
        print("some message")

class ECStudent2(Person):
    def printDeatlis(self):
        print("some message")

obj=ECStudent1()
obj.CityName="new city"
obj.printName("ECStudent1")

obj1=ECStudent2()
obj1.CityName="london"
obj1.printName("ECStudent2")