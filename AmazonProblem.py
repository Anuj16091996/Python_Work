def CheckOccurance(array, array_value):
    post=0
    for i in range(0,len(array)):
        if(array[i]==array_value):
            post=i

    return post


def FinalCode(array):
    i=0
    A=[]

    while(i<len(array)):
        groupend=CheckOccurance(array,array[i])

        for j in range(i+1,groupend):
            tempend=CheckOccurance(array,array[j])
            if(tempend>groupend):
                groupend=tempend

        A.append(groupend+1-i)
        i=groupend+1

    return A





def main():
    Datalist=["a","b","a","b","c","b","a","c","a","d","e","f","e","g","d","e","h","i","j","h","k","l","i","j"]
    print(Datalist)
    print(FinalCode(Datalist))


main()


