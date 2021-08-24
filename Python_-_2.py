
#python control flows

# write a small program to ask for a name and an age.
# when both values have been entered, check if the person
# is the right age to go to college (they must be over 18).
# if they are, welcome them to the college, otherwise print
# a polite message refusing them entry

# name = input("Please enter your name: ")
# age =  int(input("how old are you, {0}? ".format(name)))
# if age>=18 and age <80:
#     print("welcome to college! {0}".format(name))
#     #print("welcome to college!" + name)  #coercion
# else:
#     print("I'm sorry, our college is only for 18 \n"
#           " and plus and less than 80 years old people")

#Array in Python
#to work with arrays in Python we will have to import a library, like the NumPy library.
#however we could use LISTS AS ARRAYS

#Students = ["Singh","Kaur","Mandeep","Mohamed"]
#print the content of Student array object
# print(Students)
#print all elements of the array
# for item in Students:
#     print(item)
#     print()
#print all element except "Mandeep"
# for item in Students:
#     if item != "Mandeep":
#      print(item)




#array declaration (once for all, we are dealing with list.but we use it as array)
# Cars = [5,4]
# for  x in Cars:
#     print(x)
#
#
# print(len(Cars))  #2
# Cars[0] = "Toyota" #replacing array element by index
# Cars[1]= "Mercedes"
# y = len(Cars)
# print("the lenght of the array is " +  str(y))
#
# for x in Cars:
#     print(x)

# Cars = [5]
# Cars[0]= "Toyota"
# Cars.append("Honda")
# for x in Cars:
#     print(x)
#
# print("after Remove method")
# Cars.remove("Toyota")
# y = len(Cars)
# print("the lenght of array is " + str(y))
# print(Cars[0]) #shifting back elements is done automatically in array(list)
# for x in Cars:
#     print(x)



#array declaration and element replacements
# Cars = []
# Cars = ["Toyota", "Volvo","Buick"]
# Cars = ["Ford","Volvo","BMW"]
# for x in Cars:
#     print(x)


# Cars = []
# #append() adds an element at the end of the list
# Cars.append("Volvo")
# Cars.append("Mercedes")
# Cars.pop(0) #pops out the element index 0
# for x in Cars:
#     print(x)




# Cars = []
# #append() adds an element at the end of the list
# Cars.append("Volvo")
# Cars.append("Mercedes")
# #count() returns the number of elements with that specific values
# print(Cars.count("Mercedes"))


# Cars = []
# #append() adds an element at the end of the list
# Cars.append("Volvo")
# Cars.append("Mercedes")
# #extend() add the elements of the list to the end of the current list
# Cars.extend("BMW")
# for x in Cars:
#     print(x)


# Cars = ["Volvo","Mercedes","Tesla"]
# #reverse() : reverses the order ot the list
# Cars.reverse()
# for x in Cars:
#     print(x)


# Cars = ["Volvo","Mercedes","Volvo","Tesla"]
# #index(): returns the index of the first element with the specified value
# print(Cars.index("Volvo"))


# Cars = ["Volvo","Mercedes","Tesla"]
# #insert() : adds an element at the specified position
# Cars.insert(1,"Porsche")
# print("after insert")
# for x in Cars:
#     print(x)


# Cars = []
# Cars.append("Volvo")
# Cars.append("Mercedes")
# Cars.append("Volvo")
# print("-----------before sort -----------------")
# for x in Cars:
#     print(x)
# print("-------------after sort---------------")
# Cars.sort()
# for x in Cars:
#     print(x)

# Cars = ["Volvo","Mercedes","RangeRover"]
# print("------first List ------------")
# for x in Cars:
#     print(x)
# print("-----second List------------")
# Cars2 = Cars.copy()
# for x in Cars2:
#     print(x)


#if / else

# a = 2
# b = 330
# print("A") if a>b else print("B")



# a = 200
# b = 33
# c = 500
# if a>b or a > c:
#     print("at least one of the conditions is True")


# x = 41
# if x > 10:
#     print("above ten")
# if x > 20:
#     print("and also is above 20")
# else:
#     print("but not above 20")


# a = 200
# b = 33
# c = 500
# if a>b and c>a:
#     print("both conditions are True")


# a = 200
# b = 33
# if b> a:
#     print("b is greater than a")
# else:
#     print("b is NOT greater than a")

