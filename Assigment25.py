arr=[1, 2, 3, 4, 5]
k=3
print(arr)
n=len(arr)//k
arr_Final=[]
for i in range(n):
    if k>1:
        numbers = arr[0:k]
    else:
        numbers=arr[0:1]
    for j in range(k):
        arr.pop(0)
    arr_Final.extend(numbers)
    #print("arr: "+str(arr))
    #print("Arr final: "+str(arr_Final))
if len(arr)<k:
    arr_Final.extend(arr)
print("Result: "+str(arr_Final))