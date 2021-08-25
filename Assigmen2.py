
# Data Memebers
status=True
Number=[1,2,3,4,6,-9,3]

# All Function
def MenuDisplay():
    print('P - Print numbers')
    print('A - Add a number')
    print('M - Display mean of the numbers')
    print('S - Display the smallest number')
    print('L - Display the largest number')
    print('Q - Quit')
    print("AD- Additional functionality:")
    print();
    choice=input('Enter your choice:')
    return choice

def PrintNumber():
     if(len(Number)==0):
         print("[] - the list is empty")
         print()

     else:
          print(Number)
          print()

def MeanofNumber():
    if(len(Number)==0):
        print("Unable to calculate the mean - no data")
    else:
        mean=0
        for check in Number:
            mean+=check

        meanvalue=mean/len(Number)

        print(meanvalue)
    print()

def AddNumber():
    number_user=int(input("Enter The Number"))
    Number.append(number_user)

def Ask_User():
    print('Do You Want To Continue')
    print('Press 1 for Yes')
    print('Press 2 for No')
    User_Ans=int(input())
    if(User_Ans==1):
        return True

    else:
        print('Good Bye')
        return False


def SmallestNumber():
    if(len(Number)==0):
        print("Unable to calculate the mean - no data")

    else:
        min=Number[0]
        for i in range(0,len(Number)):
            if(Number[i]<min):
                min=Number[i];

    print("Smallest element present in given array: " + str(min));

    print()


def LargestNumber():
    if(len(Number)==0):
        print("Unable to calculate the mean - no data")

    else:
        max=0
        for i in range(0,len(Number)):
            if(Number[i]>max):
                max=Number[i];

    print("Largest element present in given array: " + str(max));

    print()

def AdditionalFunction():
    if(len(Number)==0):
        print("Unable to calculate the mean - no data")

    else:
        count=0
        number_users=int(input("Enter The Number"));

        for check in Number:
            if(number_users==check):
                count=count+1;

    print("Number of time found is : " + str(count));
    print()



# Final Code

while status:
    choice=MenuDisplay()



    if(choice=='p' or choice=='P'):
        PrintNumber()
        status=Ask_User()

    elif(choice=='a' or choice=='A'):
        AddNumber()
        status=Ask_User()


    elif(choice=='M' or choice=='m'):
        MeanofNumber()
        status=Ask_User()

    elif(choice=='S' or choice=='s'):
        SmallestNumber()
        status=Ask_User()

    elif(choice=='L' or choice=='l'):
        LargestNumber()
        status=Ask_User()

    elif(choice=='q' or choice=='Q'):
        print('Good Bye')
        status=False

    elif(choice=='AD' or choice=='ad' or choice=='Ad' or choice=='aD'):
        AdditionalFunction()
        status=Ask_User()

    else:
        print('Invalid Choice Try Again')
        status=True



