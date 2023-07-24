class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show1(self):
        print(f"Name = {self.name}, Age = {self.age}, ", end=" ")

class student:
    def __init__(self, rollnum, per):
        self.rollnum = rollnum
        self.per = per
    def __data(self):
        print(f"Rollnum = {self.rollnum}, percentage = {self.per}")
    def show2(self):
        self.__data()

class scienceStudent(person,student):
    def __int__(self,name,age,rollnum,per):
        super().__int__(name,age)
        super().__init__(rollnum,per)
    def __data(self):
        super().show1()
        super().show2()
        print("Student selected stream is SCIENCE")
    def show(self):
        self.__data()


nameT   = input("Enter the Name of Person:  ")
AgeT = int(input("Enter the age of Person:  "))

Rollnum = int(input("Enter the Roll num of student: "))
percentage = float(input("Enter the percentage of student:  "))

# obj1 = person(nameT,AgeT)
# obj2 = student(Rollnum,percentage)

obje3  = scienceStudent(nameT,AgeT,Rollnum,percentage)

