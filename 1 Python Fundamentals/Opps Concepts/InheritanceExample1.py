class schoolmember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name = {self.name}, Age = {self.age}, ",end = " ")
class student(schoolmember):
    def __init__(self,name,age,rollnum,per):
        super().__init__(name,age)
        self.rollnum = rollnum
        self.per = per
    def __data(self):
        super().show()
        print(f"Rollnum = {self.rollnum}, percentage = {self.per}")
    def show(self):
        self.__data()
class teacher(schoolmember):
    def __init__(self,name,age,sal):
        super().__init__(name,age)
        self.sal = sal
    def __data(self):
        super().show()
        print(f"Salary = {self.sal} ")
    def show(self):
        self.__data()

nameS  = input("Enter the Name of student :  ")
AgeS = int(input("Enter the age of student:  "))
Rollnum = int(input("Enter the Roll num of student: "))
percentage = float(input("Enter the percentage of student:  "))

nameT   = input("Enter the Name of Teacher:  ")
AgewT = int(input("Enter the age of Teacher:  "))
salary = int(input("Enter the Salary of Teacher: "))



obj = student(nameS,AgeS,Rollnum,percentage)
obj1 = teacher(nameT,AgewT,salary)

obj.show()
obj1.show()