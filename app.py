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

for i in [1,2,3]:
  print("Ali")

for i in ["Sp" ,"gre" ,"asd"]:
  print("Alicia")

for i in ["Zero" ,"One" ,"Two", "Three"]:
  print(i)

for numbers in ["Zero" ,"One" ,"Two", "Three"]:
  print(numbers)