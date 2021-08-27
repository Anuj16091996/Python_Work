#
# #creating an interface by making all methods abstracts
# class Shape:
#     def __init__(self):
#         if type(self) is Shape:
#             raise NotImplementedError('Abstract class can not be instantitated')
#
#     def draw(self):
#         pass
#
#
# class Circle(Shape):
#
#     def __init__(self):
#         super().__init__()
#
#     def draw(self):
#         print("inside Circle::draw() method")
#
#
# class Square(Shape):
#
#     def draw(self):
#         print("inside Square::draw() method")
#
#
# class Rectangle(Shape):
#
#     def draw(self):
#         print("inside Rectangle::draw() method")
#
#
# class ShapeFactory:
#
#     @classmethod
#     def getshape(cls, shapetype) -> Shape:
#         if shapetype == "CIRCLE":
#             return Circle()
#         elif shapetype == "RECTANGLE":
#             return Rectangle()
#         elif shapetype == "SQUARE":
#             return Square()
#         else:
#             return None
#
#
# class MyShapes:
#
#     def main(self):
#
#         c = ShapeFactory.getshape("CIRCLE")
#         c.draw()
#         r = ShapeFactory.getshape("RECTANGLE")
#         r.draw()
#         s = ShapeFactory.getshape("SQUARE")
#         s.draw()
#
#
# m = MyShapes()
# m.main()
#
#
#
#
#
#
#
#
# # from interface import implements, Interface
# #
# #
# # class Shape(Interface):
# #
# #     def draw(self):
# #         pass
# #
# #
# # #class Circle
# # class Circle(implements(Shape)):
# #
# #     def draw(self):
# #         print("inside Circle::draw() method.")
# #
# #
# # # class Square
# # class Square(implements(Shape)):
# #
# #     def draw(self):
# #         print("inside Square::draw() method.")
# #
# #
# # # class Rectangle
# # class Rectangle(implements(Shape)):
# #
# #     def draw(self):
# #         print("inside Rectangle::draw() method.")
# #
# #
# # class ShapeFactory:
# #
# #     def getshape(self,shapeType):
# #         if shapeType == "CIRCLE":
# #             return Circle()
# #         elif shapeType == "RECTANGLE":
# #             return Rectangle()
# #         elif shapeType == "SQUARE":
# #             return Square()
# #         else:
# #             return None
# #
# #
# # class MyShapes:
# #
# #     def main(self):
# #
# #         myshape = ShapeFactory()
# #         c = myshape.getshape("CIRCLE")
# #         c.draw()
# #         r = myshape.getshape("RECTANGLE")
# #         r.draw()
# #         s = myshape.getshape("SQUARE")
# #         s.draw()
# #
# #
# # m = MyShapes()
# # m.main()
# #
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
# # #abstract class Animal
# # class Animal:
# #     def __init__(currentobject,age,gender,weight):
# #         raise NotImplementedError("abstract class cnat be instantiated")
# #
# #     def sleep(currentobject):
# #         print("the animal is sleeping...")
# #
# #     def eat(currentobject):
# #         print("the animal is eating...")
# #
# #     def speak(currentobject):
# #         print("the animal age is " + str(currentobject.age) + " years old")
# #         print("the animal weight is " + str(currentobject.weight) + " kg")
# #         print("the animal gender is " + currentobject.gender)
# #
# #     def move(currentobject):
# #         raise NotImplementedError("put some code here")
# #
# #
# # class Bird(Animal):
# #
# #     def __init__(self,age,gender,weight):
# #         self.age = age
# #         self.gender = gender
# #         self.weight = weight
# #
# #     def move(self):
# #         print("the bird is flying...")
# #
# # #lets test this
# # # x = Bird(2,"female",6)
# # # x.speak()
# #
# #
# # class Chicken(Bird):
# #
# #     def move(self):
# #         print("the chick clapping wings...")
# #
# #
# # #lets test it
# # # x = Bird(2,"female",6)
# # # x.move()
# # # y = Chicken(3,"female",10)
# # # y.move()
# #
# #
# # from interface import implements, Interface
# #
# #
# # class Singable(Interface):
# #
# #     def sing(self):
# #         pass
# #
# #
# # class Sparrow(Bird,implements(Singable)):
# #
# #     def move(self):
# #         print("the sparrow is flying high...")
# #
# #     def sing(self):
# #         print("the sparrow is singing like Beyonce...!")
# #
# #
# # #lets test it
# # # s = Sparrow(4,"male",5)
# # # s.sing()
# #
# #
# # class Perrokee(Bird,implements(Singable)):
# #
# #     def move(currentobject):
# #         print("the Perrokee is flying from one tree to another one...")
# #
# #     def sing(self):
# #         print("the Perrokee is singing (acting) like Deepika pudokone...!")
# #
# # #testing it
# # # p = Perrokee(7,"female",3)
# # # p.move()
# # # p.sing()
# #
# #
# # class Kangaroo(Animal):
# #
# #     def __init__(self,age,gender,weight):
# #         self.age = age
# #         self.gender = gender
# #         self.weight = weight
# #
# #     def move(self):
# #         print("the Kangaroo is jumping....")
# #
# #
# # class Fish(Animal):
# #
# #     def __init__(self,age,gender,weight):
# #         self.age = age
# #         self.gender = gender
# #         self.weight = weight
# #
# #     def move(self):
# #         print("the fish is swimming....")
# #
# #
# # class Zoo:
# #
# #     def main(self):
# #         b = Bird(1,"female",10)
# #         b.move()
# #         c = Chicken(2,"female",20)
# #         c.move()
# #         s = Sparrow(3,"male",30)
# #         s.move()
# #         print("moveanimal dynamic")
# #         z = Zoo()
# #         z.moveanimal(b)
# #         z.moveanimal(c)
# #         z.moveanimal(s)
# #
# #     def moveanimal(self,animal):
# #         animal.move()
# #
# #     @staticmethod
# #     def moveAnimal(animal):
# #         animal.move()
# #
# #
# # m = Zoo()
# # m.main()
# # print("this one is static moveAnimal")
# # mySparrow = Sparrow(10,"male",100)
# # Zoo.moveAnimal(mySparrow)
#
#
#
#
#
#
# #there is no method overloading in python. so the polymorphism is kinda
# #half way done...
# #but there are ways to make it done. one of the best way is :
#
#
# #pip3 install multipledispatch
#
# # from multipledispatch import dispatch
# # #passing 2 parameters
# # @dispatch(int,int)
# # def product(first,second):
# #     result = first*second
# #     print(result);
# #
# # #passing 3 parameters
# # @dispatch(int,int,int)
# # def product(first,second,third):
# #     result = first * second * third
# #     print(result);
# #
# # #you can also pass data type of any value as per requirement
# # @dispatch(float,float,float)
# # def product(first,second,third):
# #     result = first * second * third
# #     print(result);
# #
# #
# # #calling product method with 2 and 3 arguments
# # product(4,5) #this outputs 20
# # product(2,3,2) #this will give output of 12
# # product(2.2,3.4,2.3) # this will give output of 17.204
#
