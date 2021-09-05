from random import randint
FoundList=[]

def CreatingRandomIndex():
    Rows=randint(1,10)
    Colum=randint(1,10)
    # x=[[randint(0,1) for _ in range(Rows)] for _ in range(Colum)] #This is Colum
    x=[[1,0,1,0,0],[1,0,1,1,1],[1,0,1,1,1],[1,1,0,1,0]]

    return x


def IncreadingValues():
    FoundList=[]
    Matrix=CreatingRandomIndex()
    Matrix_Lenght=len(Matrix)
    MaxArea=0
    for i in range(0,Matrix_Lenght):
        print()
        print(Matrix[i])
        if isinstance(Matrix[i],object)==True:
            lenght=len(Matrix[i])
            for j in range(0,lenght):
                if (i>=1):
                    if(Matrix[i][j]==1):
                        FoundList[j]=FoundList[j]+Matrix[i][j]

                    if(Matrix[i][j]==0):
                        FoundList[j]=FoundList[j]*Matrix[i][j]


                else:

                    FoundList.append(Matrix[i][j])
            print(FoundList)
            TempArea=MaxRectangleForHistogram(FoundList)
            MaxArea=max(TempArea,MaxArea)

    return MaxArea



def MaxRectangleForHistogram(Array):
    Max_Area=0

    hstack=[]
    pstack=[]
    Array.append(0)

    for i in range(len(Array)):
        Lastwidth=len(Array)+1
        while(len(hstack))!=0 and hstack[-1]>Array[i]:
            Lastwidth=pstack[-1]
            carea=(i-pstack.pop())* hstack.pop()
            Max_Area=max(carea,Max_Area)

        if(len(hstack)==0 or hstack[-1]<Array[i]):
            hstack.append(Array[i])
            pstack.append(min(Lastwidth,i))


    return Max_Area


def Main():

    Area=IncreadingValues()
    print("The maximal rectangle is "+str(Area))


Main()