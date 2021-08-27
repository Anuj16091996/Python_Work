#
# # #a python function which return multiple values from a method using list
# # #this function returns a list
# # def fun():
# #     str = "aghamirkarimi"
# #     return [str,len(str)]
# #
# # #lets execute the function
# # list = fun()
# # print(list)
#
#
#

Number=[1,2,4,6,[12,13,16],9,12,120]

NewList=[]

def MyFunc(i):
    if isinstance(i, list)==False:
        NewList.append(i)

    else:
        for j in i:






#
# # #another example of python function returning multiple values
# # def fun(par):
# #     return ["addition is " + str(Add(par)), "multiplication is " + str(Multiplication(par))];
# #
# # def Add(num):
# #     return num + num ;
# #
# # def Multiplication(num):
# #     return num * num ;
# #
# # #lets execute the function
# # list = fun(len("aghamirkarimi"))
# # print(list)
#
#
#
#
#
#
#
#
# # def crazy():
# #     return 'dara', 20 , ['love',[23,25], "oh la la"]
# #
# # #lets execute this crazy function
# #
# # first,second,third = crazy()
# #
# # print(first + "\t" + str(second) + "\t" + str(third))
# #
# # #lets execute this crazy and store the result in one single variable
# # sequence = crazy()
# # for i in sequence:
# #     print(i)
#
#
#
#
#
#
#
# # #create a class named Myclass, with a property called x:
# # class MyClass:
# #     x = 5
# #
# # #create an object named p1,and print the value of the property x of the object p1
# #
# # p1 = MyClass()
# # print(p1.x)
#
#
#
#
#
#
# # #we use __init__() function to assign values to object properties
# #
# # class Person:
# #     def __init__(self,fname,lname):
# #         self.firstname = fname
# #         self.lastname = lname
# #
# #     def printname(self):
# #         print(self.firstname,self.lastname)
# #
# # #use the Person class to create an object and lets execute that printname method
# # x = Person("ali","Domingo")
# # x.printname()
#
#
#
#
#
#
#
#
# #another example of using constructor
#
# # class Person:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #
# #     def myfunc(self):
# #         print("hello my name is " + self.name + " and i am " + str(self.age) + " years-old")
# #
# #
# # p1 = Person("Janette",26)
# # p1.myfunc()
# #
# # #we can modify properties on objects like following:
# # p1.age = 40
# # p1.myfunc()
# #
# # #we can delete properties on objects
# # del p1.age
# #
# # #we can delete objects by using del keyword
# # del p1
#
#
#
#
#
#
#
#
#
#
#
#
# #class definition cannot be empty, but there is a way to avoid error on compilation or interpretation time
# # class Person:
# #     pass
# #
# # b = Person()
#
#
#
#
#
#
# #to create a class that inherits the functionalities from another class , send the parent class
# #as parameter to the child
#
# # class Person:
# #     pass
# #
# #     def printname(self):
# #         print(self.firstname,self.lastname)
# #
# #
# #
# # class Student(Person):
# #     def __init__(self,fname,lname):
# #         self.firstname = fname
# #         self.lastname = lname
# #
# #
# # x = Student("Mike","Singh")
# # x.printname()
#
#
#
#
#
#
#
# #lets override the parent constructor and even another method
#
# # class Person:
# #     def __init__(this, fname,lname):
# #         this.fname = fname
# #         this.lname = lname
# #
# #     def printPerson(this):
# #         print("hello my name is " + this.lname)
# #`
# # class Student(Person):
# #     def __init__(self, xname , lname, age):
# #         Person.__init__(self,xname,lname)
# #         self.age = age
# #
# #     def printPerson(currentObject):
# #         print("hello my name is " + currentObject.fname + " " + str(currentObject.age))
# #
# #
# #
# # x = Student("Ali","Kaur",26)
# # x.printPerson()
#
#
#
#
# #easy example for understanding overriding a function in inheritance
# # class Parent():
# #     def __init__(self):
# #         self.value = 5
# #
# #     def get_value(self):
# #         return self.value
# #
# # class Child(Parent):
# #     def get_value(self):
# #         return self.value + 1
# #
# #
# # x = Child()
# # print(x.get_value())
#
#
#
#
#
#
# #python alson has a super() function that will make the child class inherit all
# #methods and properties from its parent
# #
# # class Person:
# #     def __init__(self,fname,lname):
# #         self.fname = fname
# #         self.lname = lname
# #
# #     def printPerson(currentObject):
# #         print("hello my name is " + currentObject.name)
# #
# #
# # class Student(Person):
# #     def __init__(self,fname,lname,age):
# #         super().__init__(fname,lname)
# #         self.age = age
# #         self.graduationyear = 2020
# #
# #     def printPerson(currentObject):
# #         print("hello my name is " + currentObject.fname + " " + str(currentObject.age)
# #               + " graduating on " + str(currentObject.graduationyear))
# #
# # #lets execute
# # x = Student("Ali","Belanger",26)
# # x.printPerson()
#
#
#
#
#
#
#
#
# #abstract class: is a class that the definition is NOT completed.
# #in the __init__ method of the class that we want to be an abstract class,
# #we check the "type" of the current class (self). if the type of self
# #is the base class (parent abstract) then we raise an exception.
#
# # class Base():
# #     def __init__(self):
# #         if type(self) is Base:
# #             raise Exception('Base is an abstract class and can not be instantiated directly')
# #         print('in the __init__ method of the Base class')
# #
# # class Sub(Base):
# #     def __init__(self):
# #         print('in the __init__ method of the sub class before calling __init__ of the Base class')
# #         super().__init__()
# #         print('in the __init__ method of the sub class after calling __init__ of the Base class')
# #
# # #lets create a sub object
# # subObj = Sub()
# # #baseObj = Base()  #this will raise an exception
#
#
# #another example on abstract class
# # class Abstract():
# #
# #     def nice(self):
# #         raise NotImplementedError('subclasses must override nice()')
# #
# #
# # class Derived(Abstract):
# #
# #     def nice(self):
# #         print("your're nice !")
# #
# # d = Derived()
# # d.nice()
#
#
#
#
#
#
#
#
# #another example of making a class abstract by making the constructor abstract
# # class Mother:
# #     def __init__(self,fname,lname):
# #         raise NotImplementedError('Abstract class cant be instantiated')
# #
# #     def printMother(currentObject):
# #         print("hello my name is " + currentObject.name)
# #
# #
# # class Child(Mother):
# #     def __init__(self,fname,lname,age):
# #         self.fname = fname
# #         self.lname = lname
# #         self.age = age
# #         self.weddingyear = 2020
# #
# #     def printMother(currentObject):
# #         print("hello my name is " + currentObject.fname + " " + str(currentObject.age)
# #               + " years-old and my wedding is on " + str(currentObject.weddingyear))
# #
# #
# # #lets create Child object
# # x = Child("ZayZay","Moogooloo",26)
# # x.printMother()
#
#
#
#
#
#
#
#
#
#
#
#
# # ATTENTION: I DO NOT LIKE ABC module !!!!
# # #python 3... i dont remember
# # #we could use abc module to create abstract class and use abstractmethod decorator to
# # #declare a method abstract
# #
# # from abc import ABC, abstractmethod
# #
# # class AbstractClass(ABC):
# #
# #     def __init__(self,value):
# #         self.value = value
# #         super().__init__()
# #
# #     @abstractmethod
# #     def eat(self):
# #         pass
# #
# # class Parents(AbstractClass):
# #     def eat(self):
# #         return "eat good food " + str(self.value) + " times every day"
# #
# # class Babies(AbstractClass):
# #     def eat(self):
# #         return "drink good milk " + str(self.value) + " times or more every day"
# #
# #
# # #lets create Babies and Parents objects
# # food = 3
# # mom = Parents(food)
# # print("mommy------")
# # print(mom.eat())
#
# # infant = Babies(food)
# # print("infant-----")
# # print(infant.eat())
#
#
#
#
#
#
#
#
#
#
#
#
# #python interface
# #go to env to find your python scripts installation. in my case it is in:
# #launch command prompt : cmd
# #C:\>cd "C:\Program Files (x86)\Python38-32\Scripts"
# #then you type: pip --version
# #pip install python-interface
# #you write the whole code and click on interface underlined red : install the package.
#
# # from interface import implements, Interface
# #
# # class MyInterface(Interface):
# #
# #     def method1(self,x):
# #         pass
# #
# #     def method2(self,x,y):
# #         pass
# #
# # class MyClass(implements(MyInterface)):
# #
# #     def method1(self,x):
# #         return x * 2
# #
# #     def method2(self,x,y):
# #         return x + y
#
# #lets create an object
# myInstance = MyClass()
# print(myInstance.method1(4))
# print(myInstance.method2(4,5))
