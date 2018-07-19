class Car():
  lenChassis=250
  widChassis=120
  wheels=4
  running=False

  def start(self):
    self.running=True

  def state(self):
    if(self.running):
      return "Car running"
    else:
      return "Car stopped"

my_car=Car()

print("Car length: ", my_car.lenChassis)
print("Has", my_car.wheels, "wheels")
my_car.start()
print(my_car.state())


print("--------Second car--------")

my_car2=Car()
print("Car length: ", my_car2.lenChassis)
print("Has", my_car2.wheels, "wheels")
print(my_car2.state())

