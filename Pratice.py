
# #this app will convert the number of meters to centimers
# def main():
#     #local variables
#     meters = 0.0
#     centimeters = 0.0
#
#     #get the number from user
#     meters = float(input('Enter the number of meters: '))
#
#     #display the corresponding number of centimeters
#     centimeters = meters_to_centimeters(meters)
#     print(meters, ' meters = ', centimeters, ' centimeters')
#
# #the meters_to_centimers function receives the number of meters
# #and returns the number of centimers in that many meters
# def meters_to_centimeters(meters):
#     return 100 * meters
#
# #call the main function
# main()




#
# #make an app which finds the max of two integers
# def main():
#     #local variables
#     num1 = 0
#     num2 = 0
#     #get the numbers
#     num1 = int( input('Enter number 1: '))
#     num2 = int( input('Enter number 2: '))
#
#     #display the result
#     print('the maximum number is ', maximum(num1,num2))
#
#
# def maximum(num1,num2):
#      if num1 > num2:
#          return num1
#      else:
#          return num2
#
# main()



# #remember in physics we had a formula to calculate the falling distance of an object : h =(1/2)*g*t*t
# #main function
# def main():
#     #local variable
#     distance = 0.0
#     print('Time\tFalling Distance')
#     print('----------------------')
#     #a loop for the first 10 seconds
#     for time in range(1,11):
#         distance = falling_distance(time)
#         print(time, '\t',format(distance, '.2f' ))
#
#
# def falling_distance(time):
#     fallDistance = (9.8 * time * time) / 2
#     return fallDistance
#
#
# main()


# #we want to create an app which calculates how many odd and how many even numbers we have out of 100 random numbers
# import random
# def main():
#     #local varialbes
#     currentNumber = 0
#     oddCounter = 0
#     evenCounter = 0
#     totalNumbers = 100
#
#
#     for counter in range(totalNumbers):
#         #get a random number
#         currentNumber = random.randint(1,1000)
#         #check if number is odd or even
#         if isEven(currentNumber):
#             evenCounter+=1
#         else:
#             oddCounter+=1
#
#     print('Out of ', totalNumbers, ' random numbers , ', oddCounter, ' were odd and ', evenCounter , ' were even')
#
#
# #this function returns True if number is even, False if is odd.
# def isEven(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# #calling function main
# main()



#write an app to find out if a number is a prime number.

# def main():
#     #local variables
#     number = 0
#     #get the number from user
#     number = int(input('enter an integer: '))
#     #display the result
#     if is_prime(number):
#         print('the number is prime.')
#     else:
#         print('the number is NOT prime')
#
# # this function receives a number as argument, and returns True if number is prime , false if not prime
# def is_prime(number):
#     #local varialbes
#     status = True
#     half = int(number / 2)
#     for count in range(2, half + 1):
#         if number % count == 0:
#             status = False
#             break
#     return status
#
#
# #call the main function
# main()
#


#generating a random number (1,100)
#asking the user to guess this number
#guiding the user through the game by telling him if his guess is less or bigger than the number
#playGuessingGame
# import random
# def main():
#     #local varialbes
#     number = 0
#     play = 1
#
#     while (play > 0):
#         number = random.randint(1,100)
#         play = playGuessingGame(number)
#
#     print('nice game. thanks for playing')
#
#
# def playGuessingGame(number):
#     #get the users guess
#     userGuess =  int(input('enter a number between 1 and 100, or 0 to quit  '))
#
#     #as long as player doesnt want to quit
#     while userGuess > 0:
#         if userGuess > number:
#             print('Too high, try again')
#             userGuess = int(input('enter a number between 1 and 100, or 0 to quit'))
#
#         elif userGuess < number:
#             print('Too low, try again')
#             userGuess = int(input('enter a number between 1 and 100, or 0 to quit'))
#
#         else:
#             print('you are such a smart player !')
#             return userGuess   #to start the game again
#
#
#     return userGuess #the player enters 0
#
#
# #calling the main function
# main()
#




#functions are objects. we can pass them as arguments to other functions.
#Funcations that can accept other functions as arguments, are also called HIGHER-ORDER functions.

# def student(text):
#     return "student saying: " + text.upper()
#
# def teacher(text):
#     return "teacher saying : " + text.lower()
#
# def saySomething(funcPar):
#     #storing the function in a variable
#     myStatement = funcPar("hello i love science")
#     print(myStatement)
#
# def main():
#     saySomething(student)
#     saySomething(teacher)
#
#
# main()




#another example of a function accepting function as parameter

# def Add(num1,num2):
#     return num1 + num2
#
# def Multiplication(num1,num2):
#     return num1 * num2
#
# def Division(num1,num2):
#     return num1 / num2
#
# def doCalculations(funcPar):  #dynamic typing
#     print(funcPar(6,4))
#
# def main():
#     doCalculations(Add)
#     doCalculations(Multiplication)
#     doCalculations(Division)
#
#
# main()



#example of a function accepting another function as parameter and returning a function
# def Add(num1,num2):
#     print(num1 + num2 )
#
#
# def doCalculations(Number1, Number2):
#     return Add(Number1,Number2)
#
#
# import random   #NO hoisting in Python (opposite of js)
#
# def main():
#     doCalculations(random.randint(1,10), random.randint(1,10))
#
# main()