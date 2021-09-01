from random import randint
import random

def CreatingRandomIndex():
    Rows=randint(1,10)
    x=[randint(1,10) for _ in range(Rows)] #This is Colum

    return x

def CheckingTotal(Numbers):
    Total=0
    for j in Numbers:
        Total=Total+j

    return Total


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
                print("You Are in First Array Match")
                Number2=NumberList.copy()
                print(Number2)
                for re in range(0,len(Stack)):
                    Number=NumberList[re]
                    Number2.remove(Number)


                
                print(Number2)
                return Stack
                break

            else:
                return False
            Len=Len+1
        Len=Temp
        Len-=1




def CheckTheNumber():
    Numbers=[1,5,1,4,1,2]
    FinalStatus=True
    # print(Numbers)
    Total=CheckingTotal(Numbers)
    Average=Total/len(Numbers)
    print(Average)
    # print(Total)
    num=0
    Count_Times=0
    while num<=0:

        Check=CheckArray(Numbers,Average)
        len(Numbers)
        # print(Check)

        if Check==False:
            random.shuffle(Numbers)
            Count_Times+=1
            num=0

        if Count_Times==len(Numbers):
            FinalStatus=False
            break

        else:
            num=1
            FinalStatus=True
            break

    return FinalStatus



def Main():
    Value=CheckTheNumber()
    print(Value)


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
