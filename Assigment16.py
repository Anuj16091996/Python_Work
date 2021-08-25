def latest_occurence(array, c):
    post=-1
    for i in range(0,len(array)):
        if(array[i]==c):
            post=i


    return post


def Sepration(array):
    i=0
    A=[]

    while i<len(array):
        groupend=latest_occurence(array,array[i])

        for j in range(i+1,groupend):
            tempend=latest_occurence(array,array[j])
            if(tempend>groupend):
                groupend=tempend

        A.append(groupend-i+1)
        i=groupend+1

    return A




def main():
    Datalist=["a","b","a","b","c","b","a","c","a","d","e","f","e","g","d","e","h","i","j","h","k","l","i","j"]
    print(Datalist)
    print(Sepration(Datalist))


main()

# for i in range(0, len(Datalist)):
#     item=Datalist[i]
#     lastindex=Datalist[len(Datalist)-1]
#
#     if(i==lastindex):
#         CountNumber.append(1)
#
#     else:
#         if(i==0):
#             CountNumber.append(lastindex+1)
#
#         else:
#             CountNumber.append(lastindex-i+1)
#
#         i=lastindex
#
# print(CountNumber)

#
#
# for i in range(output, len(Datalist)):
#     if(len(DataCopy)!=0):
#         CountNumber.append(len(DataCopy))
#         i=len(DataCopy)
#
#     else:
#         i=0
#     for j in range(i,len(Datalist)-1):
#
#          if(Datalist[i]==Datalist[j]):
#             for ab in range(0,j):
#              DataCopy.append(Datalist[ab])
#
#
#
#
#
#
#
#
# print(CountNumber)
#
