staus=True
Number=[1,2,9,1]
mean=0


while staus:
    print('P - Print numbers')
    print('A - Add a number')
    print('M - Display mean of the numbers')
    print('S - Display the smallest number')
    print('L - Display the largest number')
    print('Q - Quit')
    print("AD- Additional functionality:")
    print();
    choice=input('Enter your choice:')

    if(choice=='P' or choice== 'p'):

            if(len(Number)==0):
                print("[] - the list is empty")
                print('Do You Want To Continue')
                print('Press 1 for Yes')
                print('Press 2 for No')
                User_Ans=int(input())
                if(User_Ans==1):
                    staus=True
                else:
                    print('Good Bye')
                    staus=False


            else :
                    print( Number)

                    print()


    elif(choice=='a' or choice=='A'):
            number_user=int(input("Enter The Number"))
            Number.append(number_user)
            print('Do You Want To Continue')
            print('Press 1 for Yes')
            print('Press 2 for No')
            User_Ans=int(input())
            if(User_Ans==1):
                staus=True
            else:
                print('Good Bye')
                staus=False


    elif(choice=='M' or choice=='m'):
        if(len(Number)==0):
            print("Unable to calculate the mean - no data")
            print('Do You Want To Continue')
            print('Press 1 for Yes')
            print('Press 2 for No')
            User_Ans=int(input())
            if(User_Ans==1):
                staus=True
            else:
                print('Good Bye')
                staus=False
        else:
            for check in Number:
                mean+=check

            meanvalue=mean/len(Number)

        print(meanvalue)
        print()

    elif(choice=='S' or choice=='s'):
        if(len(Number)==0):
            print("Unable to calculate the mean - no data")
            print('Do You Want To Continue')
            print('Press 1 for Yes')
            print('Press 2 for No')
            User_Ans=int(input())
            if(User_Ans==1):
                staus=True
            else:
                print('Good Bye')
                staus=False

        else:
            min=Number[0]
            for i in range(0,len(Number)):
                 if(Number[i]<min):
                     min=Number[i];

        print("Smallest element present in given array: " + str(min));

        print()

    elif(choice=='L' or choice=='l'):
        if(len(Number)==0):
            print("Unable to calculate the mean - no data")
            print('Do You Want To Continue')
            print('Press 1 for Yes')
            print('Press 2 for No')
            User_Ans=int(input())
            if(User_Ans==1):
                staus=True
            else:
                print('Good Bye')
                staus=False

        else:
            max=0
            for i in range(0,len(Number)):
                if(Number[i]>max):
                    max=Number[i];

        print("Biggest element present in given array: " + str(max));

        print()

    elif(choice=='q' or choice=='Q'):
        print('Good Bye')
        staus=False

    elif(choice=='AD' or choice=='ad' or choice=='Ad' or choice=='aD'):
        if(len(Number)==0):
            print("Unable to calculate the mean - no data")
            print('Do You Want To Continue')
            print('Press 1 for Yes')
            print('Press 2 for No')
            User_Ans=int(input())
            if(User_Ans==1):
                staus=True
            else:
                print('Good Bye')
                staus=False

        else:
            count=0
            number_users=int(input("Enter The Number"));

            for check in Number:
                if(number_users==check):
                    count=count+1;

        print("Number of time found is : " + str(count));
        print()


    else:
        print("Invalid Input ! Try Again")
        print()
        staus=True
