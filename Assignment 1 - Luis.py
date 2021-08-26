import os

listOfNumbers = []
option = 1
while option != 'Q':
    option = str(input("""P - Print numbers
A - Add a number
M - Display mean of the numbers
S - Display the smallest number
L - Display the largest number
* - Search for a number in the list(Additional)
Q - Quit

Enter your choice:"""))
    option = option.upper()
    if option == "P":
        if len(listOfNumbers) == 0:
            print('[] - the list is empty')
        else:
            print(listOfNumbers)
        input()
    elif option == "A":
        listOfNumbers.append(int(input('Enter an integer to add to the list: ')))
        print("{0} added".format(listOfNumbers[len(listOfNumbers)-1]))
        input()
    elif option == "M":
        if len(listOfNumbers) == 0:
            print('Unable to calculate the mean - no data')
        else:
            mean = 0
            for i in listOfNumbers:
                mean += i
            mean /= len(listOfNumbers)
            print('Mean: {0}'.format(mean))
        input()
    elif option == "S":
        if len(listOfNumbers) == 0:
            print('Unable to determine the smallest number - list is empty')
        else:
            small = listOfNumbers[0]
            for i in listOfNumbers:
                if i > small:
                    small = i
            print('The smallest number is {0}'.format(small))
        input()
    elif option == "L":
        if len(listOfNumbers) == 0:
            print('Unable to determine the largest number - list is empty')
        else:
            large = listOfNumbers[0]
            for i in listOfNumbers:
                if i < large:
                    large = i
            print('The largest number is {0}'.format(large))
        input()
    elif option == "Q":
        print('Goodbye')
    elif option == "*":
        nToSearch = int(input("Enter an integer to search in the list:"))
        nCount = 0
        for i in listOfNumbers:
            if i == nToSearch:
                nCount += 1
        if nCount == 0:
            print('No coincidences found with {0}', nToSearch)
            input()
        else:
            print('{0} is repeated {1} times in the list', nToSearch, nCount)
            input()
    else:
        print('Unknown selection, please try again')
