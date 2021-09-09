# list
# Lists are enclosed in brackets:
l = [1, 2, "a"]
# The index() methods searches for an element in a list. For instance:
# my_list = ['a','b','c','b', 'a']
# my_list.index('b')

# The insert() methods insert an object before the index provided.
# my_list.insert(2, 'a')

# Similarly, you can remove the first occurence of an element as follows:
# my_list.remove('a')

# Or remove the last element of a list by using:
# my_list.pop()

# You can count the number of element of a kind:
# my_list.count('b')

# There is a sort() method that performs an in-place sorting:
# my_list.sort()
# A list is INTENDED (NOT ENFORCED THOUGH!) to keep  same type of objects
# A list is mutable.

#############################################################################################
# tuple
# Tuples are enclosed in parentheses:
t = (1, 2, "a")
# Tuples are faster and consume less memory.
# There are two methods available only:
# index, to find occurence of a value
# count, to count the number of occurence of a value
# t = (1,2,3,1)
# t.count(1)
# t.index(2)

# A tuple is INTENDED(EVEN TOUGH THEY COULD BE THE SAME) TO keep different type of objects
# A tuple is immutable

# set
# Sets are made using the set() builtin function.
s = set(1, 2, 3, 5)
# a set is more similar to a collection of dictionary keys, sets are less often than the other data structures
# Elements in a set must be immutable objects (similar to dictionary keys)
# Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable.
# Objects of built-in types like (list, set, dict) are mutable.
# Custom classes are generally mutable.
# Unordered (Similar to dictionary) (NO INDEX) and doesn't contain duplicates (Similar to dictionary)
# Items aren't accessed via a key (Unlike dictionary)
# To add element to the set you use add. Example
# s.add(9)

# dictionary
# Dictionaries are built with curly brackets:
d = {"a": 1, "b": 2}
# Dictionary is a collection which is unordered and mutable.
# No duplicate members(no two items with the same key).holds key-value pairs.
# Dictionary items unordered: you cannot refer to an item by using an index
# print(d["a"])

# numpy
# import numpy
# arr = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr)
#Reshaping means changing the shape of an array. The shape of an array is the number of elements in each dimension
#by reshaping we can add or remove dimenions or change the number of elements in each dimension.
# newarr=arr.reshape(5,2,5)
# print(newarr)

# #iterating a numpy array
# import numpy
# arr = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z , end = " ")
#
# #iterating with different step size
# print('##############')
# for x in numpy.nditer(arr[:,::2]):
#     print(x, end = " ")