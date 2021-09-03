def compoundInterest():
    amount = float(input('Please enter the amount: '))
    annualRate = float(input('Please enter the interest annual in percentage(%): '))
    years = float(input('Please enter the numbers of years: '))

    compoundInt = round(amount*((1 + ((annualRate/100) / 1))**(1 * years)),2)
    print('The compound interest for the amount: {0}, years: {1} and annual rate: {2}% is: \n{3}'.format(amount, years, annualRate, compoundInt))

def fibonacci():
    limit = int(input('Please the numbers of sequences  to display: '))
    value = []
    num1 = 1
    num2 = 1
    if limit <3:
        value = 1
    else:
        value.append(num1)
        value.append(num2)
        for i in range(2, limit):
            value.append(num1 + num2)
            num2 = num1
            num1 = value[i]
    print(value)

def primeNumbers():
    limitPrime = 5000
    print("List prime number until {0}".format(limitPrime))

    for i in range (1, limitPrime + 1):
        count = 0
        for j in range(2, (i//2 + 1)):
            if(i % j == 0):
                count = count + 1
                break

        if (count == 0 and i != 1):
            print("%d" %i, end = '  ')

def validateFloat(num):
    while True:
        try:
            num = float(num)
            return num
        except ValueError:
            num = input('Error: only numbers, please enter a number: ')

def validateInt(numint):
    while True:
        try:
            numint = int(numint)
            return numint
        except ValueError:
            numint = input('Error: only integer numbers, please enter an integer number: ')

def calculateGrade():
    students = validateInt(input("Please enter the number's students: "))
    nameStudents = []
    for i in range(0, students):
        nameStudents.append(input("Enter the name of student {0}: ".format(i+1)))
    gradeCourse = weightGrade()
    gradeStudent(nameStudents, gradeCourse)

def weightGrade():
    gradeCourse = []
    while True:
        try:
            print("Please enter the weight in percentage (%) for the course")
            percExam1 = validateFloat(input("(%) Exam 1: "))/100
            percExam2= validateFloat(input("(%) Exam 2: "))/100
            percAssingment1 = validateFloat(input("(%) Assingment 1: "))/100
            percAssingment2 = validateFloat(input("(%) Assingment 2: "))/100
            totalweight = percExam1 + percExam2 + percAssingment1 + percAssingment2
            while not totalweight == 1:
                print("Error: The sum of the weight must be 100%")
                percExam1 = validateFloat(input("(%) Exam 1: "))/100
                percExam2= validateFloat(input("(%) Exam 2: "))/100
                percAssingment1 = validateFloat(input("(%) Assingment 1: "))/100
                percAssingment2 = validateFloat(input("(%) Assingment 2: "))/100
                totalweight = percExam1 + percExam2 + percAssingment1 + percAssingment2
            course = [percExam1, percExam2, percAssingment1, percAssingment2]
            gradeCourse.append(course)
            break
        except ValueError:
            print('Please enter only numbers')
    return gradeCourse

def limitGrade(grad):
    while True:
        try:
            grad = float(grad)
            while grad < 0 or grad > 100:
                grad = validateFloat(input('Error: please enter a grade between 0 to 100: '))
        except ValueError:
            grad = input('Error: please enter only numbers: ')
        return grad

def gradeStudent(name, weight):
    gradeStudents = []
    for i in range(0, len(name)):
        print("\nEnter the grades for the {0} students".format(len(name)))
        print("Student: " + name[i])
        exam1 = limitGrade(validateFloat(input("Grade Exam 1: ")))
        exam2 = limitGrade(validateFloat(input("Grade Exam 2: ")))
        assingment1 = limitGrade(validateFloat(input("Grade Assingment 1: ")))
        assingment2 = limitGrade(validateFloat(input("Grade Assingment 2: ")))
        gradeStu = [exam1, exam2, assingment1, assingment2]
        gradeStudents.append(gradeStu)


    for i in range(0, len(name)):
        finalGrade = 0.00
        for j in range(0, 4):
            final = gradeStudents[i][j] * weight[0][j]
            finalGrade = finalGrade + final
        print('\nStudent: ', name[i])
        print('The final grade: ', finalGrade)
        if finalGrade >= 60:
            print("{0}: passes the course".format(name[i]))
        else:
            print("{0}: fails the course".format(name[i]))


print('------Excercise 44--------')
compoundInterest()
print('------Excercise 45--------')
fibonacci()
print('------Excercise 46--------')
primeNumbers()
print('------Excercise 47--------')
calculateGrade()