import random
counter=1

class Question:
    def __init__(self ,question,answers,correct_answer ):
        global counter
        self.counter=counter
        self.question = question
        self.answers= answers
        self.correct_answer=correct_answer
        counter +=1

qs1=Question("what is the best number between 1 to 10",['1','2','3','4','5','6','7','8','9','10'],'4')
qs2=Question("what is the best number between 10 to 100",['10','20','30','40','50','60','70','80','90','100'],'40')
qs3=Question("what is the best number between 100 to 1000",['100','200','300','400','500','600','700','800','900','1000'],'400')

qustions =[qs1,qs2,qs3]

runthegame=True
while runthegame:
    print (""""
    1.Start the game
    2.Cheating
    3.Exit/Quit
    """)
    ans=input("What would you like to do?")

    if ans=="1":
        n= random.randint(0,2)
        print(qustions[n].question)
        user_answer=input("What is your answer?")
        if user_answer==qustions[n].correct_answer:
            print("you won!")
        else:
            print("You are a loser babe ")

    elif ans=="2":
        print("\n Here all The answers")
        for i in qustions :
            print(i.question+"//and the answer is  answer : "+i.correct_answer)


    elif ans=="3":

        runthegame=False
        print("\n Goodbye")
    elif ans !="":
        print("\n Not Valid Choice Try again")
