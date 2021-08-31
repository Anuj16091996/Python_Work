
def countZeros(x):

    total_bits = 32
    res = 0
    while ((x & (1 << (total_bits - 1))) == 0):
        x = (x << 1)
        res += 1

    return res

# Driver Code
x = 101
print(countZeros(x))


# def DecToBinary(x):
#
#     NewList=[]
#     while x:
#         NewList.append(int(x%2))
#         x=int(x/2)
#     return NewList
#
# def Main():
#     ShowList=DecToBinary(6)
#     Len=len(ShowList)
#     for i in reversed(ShowList):
#         print(i,end="")
#
#
#
# Main()