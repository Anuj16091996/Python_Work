from random import randint
import random


# For Creating Random Number
def CreatingRandomIndex():
    Rows=randint(1,10)
    x=[randint(1,10) for _ in range(Rows)] #This is Colum
    return x


# For Checking Total of it
def CheckingTotal(Numbers):
    Total=0
    for j in Numbers:
        Total=Total+j

    return Total




# For Checking That Number Has The Same Median Or Not
# And Printing That To Consoloe And returing a true or false value
def CheckArray(NumberList,Average):
    Len=len(NumberList)

    if(Len % 2!=0):
         Len=int(len(NumberList)/2)+1

    else:
        Len=int(len(NumberList)/2)

    while Len >=0:
        Temp=Len

        for i in range(0,len(NumberList)):
            Num=NumberList[i]
            Stack=[]
            Stack.append(i)



            ToLimitSomeNumber=len(NumberList)

            if(ToLimitSomeNumber==2 or ToLimitSomeNumber==1):
                if ToLimitSomeNumber==1:
                    return False
                else:
                    Array1=NumberList[0]
                    Array2=NumberList[1]

                    if(Array1==Array2):
                        print("["+str(Array1)+"]")
                        print("["+str(Array2)+"]")

                        return True

                    else:
                        return False


                break

            for j in range(i+1,Len):

                Count=1
                if(i==Temp):
                    break
                Stack.append(j)

                Num+=NumberList[j]
                Count+=j
            if(i==Temp):
                break
            Num_Average=Num/Count

            if(Num_Average==Average):
                # print("You Are in First Array Match")
                Number2=NumberList.copy()
                # print(Number2)
                for re in range(0,len(Stack)):
                    Number=NumberList[re]
                    Number2.remove(Number)
                Number3=[]
                for i in  Stack:

                    Number3.append(NumberList[i])
                # print(NumberList)
                print(Number3)
                print(Number2)
                return Stack
                break

            else:
                return False
            Len=Len+1
        Len=Temp
        Len-=1



# Genrting the Matrix from Random Values
# and calling the Check Array Function
def CheckTheNumber():
    Numbers= [1,2,3,4,5,6]
    print(Numbers)
    FinalStatus=True

    Total=CheckingTotal(Numbers)
    Average=Total/len(Numbers)

    num=0
    Count_Times=0
    while num<=0:

        Check=CheckArray(Numbers,Average)
        len(Numbers)


        if Check==False:
            random.shuffle(Numbers)

            # print(Numbers)
            Count_Times+=1
            num=0

        else :
            num=1
            FinalStatus=True
            break


        if Count_Times==510:
            FinalStatus=False
            break



    return FinalStatus



def Main():
    Value=CheckTheNumber()
    if(Value==True):
        print("The Above Numbers Has The Same Average")
    else:
        print("False")


Main()



# Algo That dont work

# Len=len(Numbers)
# if(Len % 2!=0):
#     Len=int(len(Numbers)/2)+1
#
# else:
#     Len=int(len(Numbers)/2)
#
#
#
# while Len >=0:
#     Temp=Len
#
#     for i in range(0,len(Numbers)):
#         Num=Numbers[i]
#         Stack=[]
#         Stack.append(i)
#
#         for j in range(i+1,Len):
#             if(i==Temp):
#                 break
#             Count=1
#             Stack.append(j)
#
#             Num+=Numbers[j]
#             Count+=j
#         if(i==Temp):
#             break
#         Num_Average=Num/Count
#
#         if(Num_Average==Average):
#             CheckStatus=True
#             break
#
#         else:
#             CheckStatus=False
#         Len=Len+1
#     Len=Temp
#     Len-=1
#
# return CheckStatus
