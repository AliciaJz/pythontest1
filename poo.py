# class Car():

#   def __init__(self):

#     self.__lenChassis=250
#     self.__widChassis=120
#     self.__wheels=4
#     self.__running=False

#   def start(self, run):
#     self.__running=run

#     if(self.__running):
#       check=self.__checking()

#     if(self.__running and check):
#       return "Car running"

#     elif(self.__running and check==False):
#       return "Something is wrong, can't run car"

#     else:
#       return "Car stopped"

#   def state(self):
#     print("Car has", self.__wheels, "wheels, a width of", self.__widChassis, "and length of", self.__lenChassis)

#   def __checking(self):
#     print("Checking car")

#     self.gas="ok"
#     self.oil="ok"
#     self.doors="closed"

#     if(self.gas=="ok" and self.oil=="ok" and self.doors=="closed"):
#       return True
    
#     else:
#       return False

# my_car=Car()

# print(my_car.start(True))

# my_car.state()

# print("--------Second car--------")

# my_car2=Car()

# print(my_car2.start(False))

# my_car2.state()

# class Vehicles():
#   def __init__(self, brand, model):

#     self.brand=brand
#     self.model=model
#     self.running=False
#     self.accelerating=False
#     self.stoping=False

#   def start_car(self):
#     self.running=True

#   def accelerate(self):
#     self.accelerating=True

#   def stop_car(self):
#     self.stoping=True
  
#   def state(self):
#     print("Brand: ", self.brand, "\nModel: ", self.model, "\nRunning: ", self.running, "\nAccelerating: ", self.accelerating, "\nStoping: ", self.stoping,)

# class Minivan(Vehicles):
#   def carry(self, carry):
#     self.carried=carry
#     if(self.carried):
#       return "Minivan is carring something"
#     else:
#       return "Minivan is carring nothing"

# class Motorcycle(Vehicles):
#   front_wheel=""
#   def horsey(self):
#     self.front_wheel="Running using only one wheel"

#   def state(self):
#     print("Brand: ", self.brand, "\nModel: ", self.model, "\nRunning: ", self.running, "\nAccelerating: ", self.accelerating, "\nStoping: ", self.stoping, "\nSpecial method: ", self.front_wheel)

# class Electric_vehicles():
#   def __init__(self):
#     self.autonomy=100

#   def charge_battery(self):
#     self.charging=True

# my_motorcycle1=Motorcycle("Lou's", "bike")

# my_motorcycle1.horsey()

# my_motorcycle1.state()


# my_minivan1=Minivan("Deb's", "van")

# my_minivan1.start_car()
# my_minivan1.state()
# print(my_minivan1.carry(True))

# class Electric_bike(Electric_vehicles, Vehicles):
#   pass

# my_electricbike1=Electric_bike()

class Person():
  def __init__(self, name, age, city):
    
    self.name=name
    self.age=age
    self.city=city

  def description(self):
    print("Name:", self.name, " Age:", self.age, "Residency:", self.city)

class Employee(Person):
  def __init__(self, salary, years, employee_name, employee_age, employee_years):

    super().__init__(employee_name, employee_age, employee_years)

    self.salary=salary
    self.years=years

  def description(self):
    super().description()
    print("Salary:", self.salary, " Years working:", self.years)

Carol=Employee(1500, 1, "Carol", 45, "NY")
Carol2=Person("Carol", 45, "NY")

Carol.description()
Carol2.description()

print(isinstance(Carol, Employee))
print(isinstance(Carol, Person))
print(isinstance(Carol2, Employee))
print(isinstance(Carol2, Person))