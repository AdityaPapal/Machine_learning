class vehicle:
    def __init__(self,name,fuel_type, topSpeed):
        self.name = name
        self.fuel_type = fuel_type
        self.topSpeed = topSpeed
    def display(self):
        print(f"Name of vehicle: {self.name}")
        print(f"Fuel type of vehicle is {self.fuel_type}")
        print(f"Top Speed of vehicle is {self.topSpeed} m/s")

name = input("Enter the name of vehicle: ")
ftype = input("Enter the fuel type of vehicle: ")
topspeed = int(input("Enter the top speed of vehicle: "))

car = vehicle(name,ftype,topspeed)
car.display()

