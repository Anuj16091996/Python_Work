# # Question9_1
# car = {"toyota": "orange",
#        "ford": "red" ,
#        "mercedes": "yellow",
#        "lexus": "green",
#        "ford": "white" ,
#        "gmc": "black"}
#
# print(car)
# user_order=input("please entet you car name : ")
# for key ,value in car.items():
#     if user_order == key:
#         print(value)
#
#
#
# # Question2
# class auto:
#     def __init__(self,model,cylinder):
#         self.model=model
#         self.cylinder=cylinder
#
#     @property
#     def print_info(self):
#         return '{},{}'.format(self.model,self.cylinder)
#
#     @property
#     def get_modle(self):
#         return '{}'.format(self.model)
#
#     @property
#     def get_cylinder(self):
#         return '{}'.format(self.cylinder)
#
#     @property
#     def start_engine(self):
#         return 'start the engine'
#
#     @property
#     def accelerate_engine(self):
#         return 'accelerating the engine'
#
#     @property
#     def break_engine(self):
#         return 'breaking the engine'
#
# class bmw(auto):
#     def __init__(self,name):
#         auto.__init__(self,model="z4",cylinder="rrs")
#         self.name=name
#     @property
#     def start_engine(self):
#         return 'bmw start the engine'
#
#     @property
#     def accelerate_engine(self):
#         return 'bmw accelerating the engine'
#
#     @property
#     def break_engine(self):
#         return 'bmw breaking the engine'
#
# class porsche(auto):
#     def __init__(self,name):
#         auto.__init__(self,model="panamara",cylinder="ffx")
#         self.name=name
#     @property
#     def start_engine(self):
#         return 'porsche start the engine'
#
#     @property
#     def accelerate_engine(self):
#         return 'porsche accelerating the engine'
#
#     @property
#     def break_engine(self):
#         return 'porsche breaking the engine'
#
# class mercedes(auto):
#     def __init__(self,name):
#         auto.__init__(self,model="Class g",cylinder="LLp")
#         self.name=name
#     @property
#     def start_engine(self):
#         return 'mercedes start the engine'
#
#     @property
#     def accelerate_engine(self):
#         return 'mercedes accelerating the engine'
#
#     @property
#     def break_engine(self):
#         return 'mercedes breaking the engine'
#
# car1=bmw("m8")
# print("Modle:"+car1.get_modle)
# print(car1.accelerate_engine)
# print(car1.break_engine)
# print("_________________________________________________________")
#
# car2=porsche("GY")
# print("Modle:"+car2.get_modle)
# print(car2.accelerate_engine)
# print(car2.break_engine)
# print("_________________________________________________________")
#
#
# car3=mercedes("pyru")
# print("Modle:"+car3.get_modle)
# print(car3.accelerate_engine)
# print(car3.break_engine)
#
# # question3


class Rates:

    def __init__(self, fname,lname,year_of_birth, current_year):
        self.fname = fname
        self.lname= lname
        self.year_of_birth=year_of_birth
        self.current_year =current_year

    @property
    def Get_fname(self):
        return self.fname
    def Set_fname(self, x):
        self.fname = x
    @property
    def Get_lname(self):
        return self.lname
    def Set_lname(self, x):
        self.lname = x
    @property
    def Get_yearOfbirth(self):
        return self.year_of_birth
    def Set_yearOfbirth(self, x):
        self.year_of_birth = x
    @property
    def Get_currentYear(self):
        return self.current_year
    def Set_currentYear(self, x):
        self.current_year = x
    @property
    def Get_real_age(self):
        return (int(self.current_year)-int(self.year_of_birth))
    @property
    def maximum_heart_ate(self):
        return (220-self.Get_real_age)*0.85
    @property
    def minimum_heart_ate(self):
        return (220-self.Get_real_age)*0.5

unit1= Rates("parsa","Rafiee",1997,2021)
unit1.Set_fname("ali")
print(unit1.Get_real_age)
print(unit1.Get_fname)
print(unit1.Get_lname)
print(unit1.maximum_heart_ate)
print(unit1.minimum_heart_ate)




