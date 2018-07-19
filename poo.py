class Car():

  def __init__(self):

    self.__lenChassis=250
    self.__widChassis=120
    self.__wheels=4
    self.__running=False

  def start(self, run):
    self.__running=run

    if(self.__running):
      return "Car running"
    else:
      return "Car stopped"

  def state(self):
    print("Car has", self.__wheels, "wheels, a width of", self.__widChassis, "and length of", self.__lenChassis)

my_car=Car()

# print("Car length: ", my_car.__lenChassis)
# print("Has", my_car.__wheels, "wheels")
print(my_car.start(True))
my_car.state()


print("--------Second car--------")

my_car2=Car()
# print("Car length: ", my_car2.lenChassis)
# print("Has", my_car2.wheels, "wheels")
print(my_car2.start(False))
my_car2.wheels=5
my_car2.state()

