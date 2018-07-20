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

class Vehicles():
  def __init__(self, brand, model):

    self.brand=brand
    self.model=model
    self.running=False
    self.accelerating=False
    self.stoping=False

  def start_car(self):
    self.running=True

  def accelerate(self):
    self.accelerating=True

  def stop_car(self):
    self.stoping=True
  
  def state(self):
    print("Brand: ", self.brand, "\nModel: ", self.model, "\nRunning: ", self.running, "\nAccelerating: ", self.accelerating, "\nStoping: ", self.stoping,)

class Motorcycle(Vehicles):
  pass

my_motorcycle1=Motorcycle("Lou's", "bike")

my_motorcycle1.state()