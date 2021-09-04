#########################################################################
#############                  Dictionnaries                ############
########################################################################

# List is a collection which is ordered and mutable. Allows duplicate members.
# Tuple is a collection which is ordered and immutable. Allows duplicate members.
# Set is a collection which is unordered,unindexed and mutuble. No duplicate members.
# Dictionary is a collection which is unordered and mutable.
# No duplicate members(no two items with the same key).holds key-value pairs.

#the values of items could be any data type
dictKeyString = {
  "string": "Ford",
  "string2": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#
# for key in dictKeyString:
#     # if isinstance(dictKeyString[key],list) :
#     #    print('--list--')
for element in dictKeyString:
    print(element, end=' ')

#
# print()
# print('before ' + str(hex(id(dictKeyString))))
# dictKeyString["year"]=2000
# print('after  ' + str(hex(id(dictKeyString))))



#no duplicate member ! Dictionaries cannot have two items with the same key.
# dictKeyNumber = {
#   1: "Ford",
#   1: "Mustang",
#   3: 1964
# }
# print(dictKeyNumber) #no duplicate member !


# #dictionary items unordered: you cannot refer to an item by using an index.
#the second occurrence overrides the first.
#print(dictKeyNumber[1]) #doesnt see the first one 1:"Ford"


# #Dictionary Length
# print(len(dictKeyNumber))
# print(len(dictKeyString))


# #dictionary type is <class 'dict'>
# print(type(dictKeyString))



#you can use an integer, float, string, or Boolean as a dictionary key. However,
# list or another dictionary can NOT serve as a dictionary key, because lists
# and dictionaries are mutable. key must be immutable. Values, on the other hand,
# can be any type and can be used more than once.

#from python documentation:
#A dictionaryâ€™s keys are almost arbitrary values. types that are not hashable, that
#is, types such as lists, dictionaries , set or other mutable types (that are compared by
# value rather than by object identity) may not be used as keys.






#2D dictionary
# dict2D = {'d1' : {'firstName1':'dara', 'lastName1':'aghamirkarimi', 'sexe1':'male'},
#           'd2' : {'firstName2':'shruta', 'lastName2':'kaur', 'sexe2':'female'},
#           'd3' : {'firstName3':'james', 'lastName3':'singh', 'sexe3':'male'}
#           }

#print(dict2D['d1']['firstName1'])
#print(dict2D['d3']['sexe3'])

# for key2 in dict2D:
#     print('--next key is ' + str(key2))
#     for key1 in dict2D[key2]:
#            print('for key ' + str(key1) + ' the value is ' + str(dict2D[key2][key1]))








# #3D dictionary
# dict3D ={
#     'd3DOne': {'d1' : {'firstName1':'dara', 'lastName1':'aghamirkarimi', 'sexe1':'male'},
#                'd2' : {'firstName2':'shruta', 'lastName2':'kaur', 'sexe2':'female'},
#                'd3' : {'firstName3':'james', 'lastName3':'singh', 'sexe3':'male'}
#           },
#     'd3DTwo': {'d4' : {'firstName4':'dara', 'lastName4':'aghamirkarimi', 'sexe4':'male'},
#                'd5' : {'firstName5':'shruta', 'lastName5':'kaur', 'sexe5':'female'},
#                'd6' : {'firstName6':'james', 'lastName6':'singh', 'sexe6':'male'}
#           }
# }


# for key3 in dict3D:
#     print()
#     print('KEY:{0} '.format(str(key3)))
#     for key2 in dict3D[key3]:
#            print()
#            print('KEY: {0} VALUE: {1}'.format(str(key2),str(dict3D[key3][key2])))
#            for key1 in dict3D[key3][key2]:
#                print('KEY: {0} VALUE: {1}'.format(str(key1), str(dict3D[key3][key2][key1])))







# #the key of  items could be any data type except that type MUST BE IMMUTABLE and HACHABLE
#An object is said to be hashable if it has a hash value that remains the same during its lifetime.

# dictKeyMixedType = {
#   "string": "Ford",
#    "2": "Mustang",
#   "year": 1964,
#   "colors": ["red", "white", "blue"],
#     #{"sheep":1, "cow":2, "hen":3}:"myDict",
#   #{"sheep", "cow", "hen"}:"mySet",
#    #["red", "white", "blue"]:"myList",
#    ("apple", "banana", "cherry"):"myTuple"
# }

# print('-----KEY------')
# for key in dictKeyMixedType:
#     print('KEY: {0} '.format( str(key)))
#
# print('-----VALUE------')
# for key in dictKeyMixedType:
#     print('VALUE: {0} '.format(str(dictKeyMixedType[key])))


# print(40 * '#')
# # #.items(), which is a method that returns a new view of the dictionaryâ€™s items:
# print("\n{: <35}  {: <30} ".format("KEY","VALUE"))
# for key, value in dictKeyMixedType.items():
#     print("{: <35}  {: <30} ".format(str(key),str(value)))











# data = [['a', 'b', 'c'], ['aghamirkarimi', 'b', 'c'], ['a', 'dara', 'c']]
#
# col_width = max(len(word) for row in data for word in row) + 2  # padding
# for row in data:
#     print(  "".join(word.ljust(col_width) for word in row))








# car = {"toyota": "orange",
#          "ford": "red" ,
#          "mercedes": "yellow",
#          "lexus": "green",
#          "gmc": "black"}
# print(car) # displays the whole dictionary
# print(car["ford"]) #displays the value of key "ford"
# # So it does NOT working by index
# #adding an element to the dictionary
# car["bmw"] = "a different nice car"
# print(car)


#adding an element to the dictionary which the key exists !
# car["lexus"] = "great car"
# print(car) #WHY??


# car = {"toyota": "orange",
#        "ford": "red" ,
#        "mercedes": "yellow",
#        "lexus": "green",
#        "ford": "white",
#        "gmc": "black"}
# print(car)
# #Taking the last entry!!




# car = {"toyota": "orange",
#        "ford": "red" ,
#        "mercedes": "yellow",
#        "lexus": "green",
#        "ford": "white" ,
#        "gmc": "black"}
#
# del car["ford"]
# print (car)
# #deletes entry!!



# car = {"toyota": "orange",
#        "ford": "red" ,
#        "mercedes": "yellow",
#        "lexus": "green",
#        "ford": "white" ,
#        "gmc": "black"}
# car.clear()
# print (car)
# #empty dictionary!!

# del car
# print (car)
# #Error!! WHY??





#items()  gives a view to the object. this view is dynamic !

# car = {"toyota": "orange",
#        "ford": "red" ,
#        "mercedes": "yellow",
#        "lexus": "green",
#        "ford": "white" ,
#        "gmc": "black"}

# #Iterating in a dictionary
#
# for key in car:
#     print(str(key))
#
# print()
#
# for key,color in car.items():
#     print(str(key) , str(color))







# Exercice : make a script that asks a user a fruit name. then searches that fruit in the fruit
# dictionary and if it finds it among the dictionary keys, it displays its value.


# fruit = {"orange": "a sweet, orange, citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour, yellow citrus fruit",
#          "grape": "a small, sweet fruit growing in bunches",
#          "lime": "a sour, green citrus fruit" }
# print (fruit)


# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)



# #shorter version
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "we dont have a " + dict_key)
#     print(description)









#########END OF DICTIONARY ############################################################################



