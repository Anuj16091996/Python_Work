def Non_Negative_Number(n):
    Values=[]
    if(n<0):
        V=abs(n)
        for i in range(1,V+1):
            Values.append(i)


    return Values


def Main():
    Status=True
    while Status:
        Number=int(input("Enter The Number-: "))
        CheckUser=Non_Negative_Number(Number)
        if(len(CheckUser)==0):
            print("Invalid Input")
            Status=True

        else:
            FinalValue=1
            SaveString=""
            for i in CheckUser:
                if(i==len(CheckUser)):
                    SaveString+=str(i)+ " = "
                    FinalValue*=i
                    break
                SaveString+=str(i)+ " * "

                FinalValue*=i
            print(SaveString+" "+ str(FinalValue))
            Status=False



Main()

