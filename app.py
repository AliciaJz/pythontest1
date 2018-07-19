# a = 0
# for i in range(5):
#   a+=1
#   print(a)


# def message():
#   print("message1")
#   print("message2")
#   print("message3")

# message()

# def summation(num1, num2):
#   print(num1+num2)

# summation(5, 7.3)

# summation(7, 9)

# summation(9, 9)

# def summation(num1, num2):
#   resultado=(num1+num2)
#   return resultado

# print(summation(5, 7.3))

# my_list=["Lore", "Betty", "Alicia", "Virgin"]

# my_list.append("Din")
# my_list.insert(2, "Din")
# my_list.extend(["Norma", "Silvia", "Raul"])

# print(my_list[:])
# my_list.pop()

# print(my_list[:])
# print(my_list[0])
# print(my_list[-1])
# print(my_list[0:2])
# print(my_list[:2])
# print(my_list[2:])
# print(my_list.index("Alicia"))
# print("Norma" in my_list)
# print("Laura" in my_list)

# my_list.remove("Din")
# print(my_list[:])

# my_list_1=[5, True, 7.9]

# my_list_2=[5, True, 7.9] * 3
# print(my_list_2[:])

# all_lists=my_list+my_list_1
# print(all_lists[:])

# my_tuple=("Alicia", 13,7,79, "Alicia", "Alicia")
# print(my_tuple)
# my_list_tuple=list(my_tuple)
# print(my_list_tuple)

# my_list_tuple1=["Alicia", 13,7,79]
# print(my_list_tuple1)
# my_tuple1=tuple(my_list_tuple1)
# print(my_tuple1)

# print("Alicia" in my_tuple)

# print(my_tuple.count(13))
# print(my_tuple.count("Alicia"))

# print(len(my_tuple))

# my_tuple=("Alicia", 13,7,79)
# name, day, month, year= my_tuple

# print(name)
# print(year)
# print(month)
# print(day)

# my_dictionary={"Alemania":"Berlin", "Francia":"Paris", "UK":"London"}
# print(my_dictionary)
# my_dictionary["Italia"]="Mexico"
# print(my_dictionary)
# my_dictionary["Italia"]="Rome"
# print(my_dictionary)
# print(my_dictionary["Francia"])

# del my_dictionary["UK"]
# print(my_dictionary)

# my_dictionary1={"Alemania":"Berlin", 3:"Paris", "UK":9}
# print(my_dictionary1)

# una_tuple=["Francia", "UK", "Mexico"]
# print(una_tuple)
# my_dictionary2={una_tuple[0]:"Paris", una_tuple[1]:"London", una_tuple[2]:"Mexico"}
# print(my_dictionary2)

# my_dictionary3={23:"Jordan", "Name":"Michael", "Team":"Chicago", "Wins":[1991, 1992, 1993, 1996, 1997, 1998]}
# my_dictionary4={23:"Jordan", "Name":"Michael", "Team":"Chicago", "Wins":{"years":[1991, 1992, 1993, 1996, 1997, 1998]}}
# print(my_dictionary3)
# print(my_dictionary3["Team"])
# print(my_dictionary3["Wins"])
# print(my_dictionary4)
# print(my_dictionary4["Wins"])
# print(my_dictionary3.keys())
# print(my_dictionary3.values())
# print(len(my_dictionary3))

# print("Grading function")

# grade_student=input("Write your grade: ")

# def evaluation(grade):
#   value="pass"
#   if grade < 5:
#     value= "failed"
#   return value

# print(evaluation(3))
# print(evaluation(9))
# print(evaluation(int(grade_student)))

# print("Can you enter here?")

# user_age=int(input("Enter your age: "))

# if user_age<18:
#   print("Come back in a few years...")
# elif user_age>99:
#   print("Yeah right...")
# else:
#   print("Please enter")

# print("Bye")

# age=233

# if 0<age<100:
#   print("good")
# else:
#   print("bu")

# print("Classes")
# print("Class: Class a - Class b - Class c")
# option=input("What class do you choose?: ")

# assign=option.lower()

# if assign in ("class a", "class b", "class c"):

#   print("You choose " + assign)

# else:

#   print("That's not a class")

# for i in [1,2,3]:
#   print("Ali")

# for i in ["Sp" ,"gre" ,"asd"]:
#   print("Alicia")

# for i in ["Zero" ,"One" ,"Two", "Three"]:
#   print(i)

# for numbers in ["Zero" ,"One" ,"Two", "Three"]:
#   print(numbers)

# for numbers in ["Zero" ,"One" ,"Two", 3]:
#   print(numbers, end=" ")

# for i in "Alicia":
  # print("Zi")
  # print("Zi", end="")

# counter=0
# my_email=input("Write your email: ")
# for i in my_email:
#   if(i=="@" or i=="."):
#     counter=counter+1

# if counter==2:
#   print("Correct email")
# else:
#   print("That's not and email")

# for i in range(7):
#   print("A")
#   print(i)

# for i in range(5):
#   print(f"index {i}")

# for i in range(7,13):
#   print(f"index {i}")

# for i in range(5,50, 3):
#   print(f"index {i}")

# valid=False
# email=input("Enter your email: ") 
# for i in range(len(email)):

#   if email[i]=="@":
#     valid=True

# if valid:
#   print("correct")

# else:
#   print("incorrect")


# i=1

# while i<=10:
#   print("Number "+ str(i))
#   i=i+1

# print("While Done")

# age=int(input("Enter your age: "))

# while age<0:
#   print("What??? are you a zombie?")
#   edad=int(input("Enter your correct age: "))

# print("OK")
# print("You say you are " + str(age))

# age=int(input("Enter your age: "))

# while age<5 or age>100:
#   print("What??? you are a baby o a really old person, go to bed")
#   edad=int(input("Enter your correct age: "))

# print("OK")
# print("You say you are " + str(age))

# import math

# print("Square root")
# number=int(input("Your number: "))

# tries=0

# while number<0:
#   print("Wrong, that is a negative number")

#   if tries==2:
#     print("Run the program again, I'm tired")
#     break;

#   number=int(input("Your number: "))
#   if number<0:
#     tries=tries+1

# if tries<2:
#   solution=math.sqrt(number)
#   print("Square root of " + str(number) + " is " + str(solution))

# for letter in "Python":
#   if letter=="h":
#     continue
#   print("Letter: " + letter)


# name="Alicia Juarez"
# counter=0

# for i in name:
#   counter+=1

# print(counter)

# name="Alicia Juarez"
# counter=0

# for i in name:
#   if i==" ":
#     continue
#   counter+=1

# print(counter)

# while True:
#   pass

# class my_class:
#   pass

# email=input("Enter your email: ")

# for i in email:

#   if i=="@":

#     at=True
#     break;

# else:

#   at=False

# print(at)

def gen_even(limit):
  num=1

  my_list_3=[]

  while num<limit:
    my_list_3.append(num*2)
    num+=1

  return my_list_3

print(gen_even(10))


def gen_even(limit):
  num=1

  while num<limit:
    yield num*2
    num+=1

ret_even=gen_even(10)

for i in ret_even:

  print(i)
  
def gen_even(limit):
  num=1

  while num<limit:
    yield num*2
    num+=1

ret_even=gen_even(10)

print(next(ret_even))
print("more code...")
print(next(ret_even))
print("more code...")
print(next(ret_even))


def ret_cities(*cities):
  for elem in cities:
    yield elem

ret_cities=ret_cities("Alberta", "Calgary", "Montreal", "Vancouver")
print(next(ret_cities))
print(next(ret_cities))

def ret_cities(*cities):
  for elem in cities:
    for subElem in elem:
      yield subElem

ret_cities=ret_cities("Alberta", "Calgary", "Montreal", "Vancouver")
print(next(ret_cities))
print(next(ret_cities))

def ret_cities(*cities):
  for elem in cities:
    yield from elem

ret_cities=ret_cities("Alberta", "Calgary", "Montreal", "Vancouver")
print(next(ret_cities))
print(next(ret_cities))
