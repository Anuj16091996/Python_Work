

def GenratePlainDromes(n):


    for j in range(0,n):
        temp=j
        reverse_num=0

        while temp>0:
            rem=temp%10
            temp=int(temp/10)
            reverse_num=int(reverse_num*10+rem)

        if(j==reverse_num):
            print(j,end=" ")





def main():
    n=123
    GenratePlainDromes(n)



main()





# Algo That Didint Work
# def CreatePlainDrome(input, b, IsOdd):
#     n=input
#     palin=input
#
#     if(IsOdd==1):
#         n=n/b
#
#     while(n>0):
#         palin=int(palin*b+(n%b))
#         n=int(n/b)
#
#
#
#
#
#     return palin
# i=1
# num=CreatePlainDrome(i,10,j%2)
# while num < n:
#     print (num),
#     i=i+1