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

my_tuple=("Alicia", 13,7,79, "Alicia", "Alicia")
print(my_tuple)
my_list_tuple=list(my_tuple)
print(my_list_tuple)

my_list_tuple1=["Alicia", 13,7,79]
print(my_list_tuple1)
my_tuple1=tuple(my_list_tuple1)
print(my_tuple1)

print("Alicia" in my_tuple)

print(my_tuple.count(13))
print(my_tuple.count("Alicia"))

print(len(my_tuple))

my_tuple=("Alicia", 13,7,79)
name, day, month, year= my_tuple

print(name)
print(year)
print(month)
print(day)