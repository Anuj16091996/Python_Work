WordList=["hot","dot","dog","lot","log","cog"]

def ToCheckForPresent(end):


    for i in range(0,len(WordList)):
        if(end==WordList[i]):
            return True

def CreatingDictonary(TempStack,Temp,Stack,EndWord):
    Dict=""
    MaxValue=0

    for i in TempStack:

        Value=0
        for j in i:

            for a in Temp:

                if(a==j):
                    Value+=1


        if(MaxValue==0):
            if(Temp!=i):
                MaxValue=Value
                Dict=i
                Value=0


        for abc in Stack:
            if(i!=abc):
                if(Value>=MaxValue):
                    ValidateValue=0
                    if(Value==MaxValue):
                        for ab in i:
                            for jc in EndWord:
                                if ab==jc:
                                    ValidateValue=ValidateValue+1
                        if(ValidateValue>=MaxValue):
                            Dict=i
                            break

                    else:
                        Dict=i
                        MaxValue=Value
                        break
        Lenght_Dict=len(Dict)-1

        if Dict==EndWord and MaxValue==Lenght_Dict:
            break


    return Dict



def CheckingandCrearting(Temp,SetofWords):
    TempStack=[]
    for i in Temp:
        new=i
        for j in SetofWords:

            for c in j:
                if (new==c):
                    if(len(TempStack)==0):
                        TempStack.append(j)
                        SetofWords.remove(j)
                        break

                    else:
                        for abc in TempStack:
                            if(abc!=j):
                                TempStack.append(j)
                                SetofWords.remove(j)
                                break


    return TempStack

def FindingThePossiblity(start,end):
    Temp=start
    Stack=[]

    while Temp:
        SetofWords=WordList.copy()
        Stack.append(Temp)
        if(Temp==end):
            return Stack
            break
        TempStack=[]
        TempStack=CheckingandCrearting(Temp,SetofWords)

        Change_Value=CreatingDictonary(TempStack,Temp,Stack,end)
        Temp=Change_Value

        for jo in WordList:
            if(jo==Temp):
                WordList.remove(jo)










def Main():
    BeginWord="hit"
    EndWord="cog"
    Status=ToCheckForPresent(EndWord)
    if Status==True:
        Stack=FindingThePossiblity(BeginWord,EndWord)
        print(Stack)

    else:
        print("Invalid Output")


Main()



# Algo that didnt work

# elif(Value>=MaxValue):
#
#     Dict=i
#     break


# else:
#     if MaxValue >2:
#         if(Temp!=i):
#             for abc in Stack:
#                 if(i==EndWord and Value>MaxValue):
#                     Dict=i
#                     break
#
#                 elif(Value>MaxValue):
#                     Dict=i
#                     break

