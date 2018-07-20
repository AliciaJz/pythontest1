class Car():

  def __init__(self):

    self.__lenChassis=250
    self.__widChassis=120
    self.__wheels=4
    self.__running=False

  def start(self, run):
    self.__running=run

    if(self.__running):
      check=self.__checking()

    if(self.__running and check):
      return "Car running"

    elif(self.__running and check==False):
      return "Something is wrong, can't run car"

    else:
      return "Car stopped"

  def state(self):
    print("Car has", self.__wheels, "wheels, a width of", self.__widChassis, "and length of", self.__lenChassis)

  def __checking(self):
    print("Checking car")

    self.gas="ok"
    self.oil="ok"
    self.doors="closed"

    if(self.gas=="ok" and self.oil=="ok" and self.doors=="closed"):
      return True
    
    else:
      return False


my_car=Car()

print(my_car.start(True))

my_car.state()

print("--------Second car--------")

my_car2=Car()

print(my_car2.start(False))

my_car2.state()

