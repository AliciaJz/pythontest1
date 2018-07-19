class Car():

  def __init__(self):

    self.lenChassis=250
    self.widChassis=120
    self.wheels=4
    self.running=False

  def start(self, run):
    self.running=run

    if(self.running):
      return "Car running"
    else:
      return "Car stopped"

  def state(self):
    print("Car has", my_car.wheels, "wheels, a width of ", self.widChassis, "and length of", self.lenChassis)

my_car=Car()

print("Car length: ", my_car.lenChassis)
print("Has", my_car.wheels, "wheels")
print(my_car.start(True))
my_car.state()


print("--------Second car--------")

my_car2=Car()
print("Car length: ", my_car2.lenChassis)
print("Has", my_car2.wheels, "wheels")
print(my_car2.start(False))
my_car2.state()

