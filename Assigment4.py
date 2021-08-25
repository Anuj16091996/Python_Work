def NumberCheck(num):
    final_number=0
    for x in range(1,num):
        if(num % x==0):
            print(x, end=" "),
            final_number+=x


    print()
    return final_number



def checkRelation(num1, num2):

    number1=NumberCheck(num1)
    print("Total of "+str(num1)+" is- " +str(number1))
    print()

    number2=NumberCheck(num2)
    print("Total of "+str(num2)+" is- " +str(number2))
    print()

    if(num1==number2 and num2==number1):
        return True

    else:
        return False



def main():
    status=checkRelation(220,284)

    if(status==True):
        print("Pair of Number Has Realtion ")

    else:
        print("They Dont share Relation")


main()

