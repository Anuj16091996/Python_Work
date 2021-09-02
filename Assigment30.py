def reversePairs():
    print("start")
    nums = [2,4,3,5,1]
    print(nums)
    if (nums == None or len(nums) == 0):
        print("return cero")
        return 0
    print("nums: "+str(nums)+"left: "+str(0)+"right"+str(len(nums)-1))
    return mergeSort(nums, 0, len(nums) - 1)

def mergeSort (nums, left, right):
    if left >= right:
        return 0;
    mid = left + ((right - left) >> 1)
    return mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right) + merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    helper = [right - left + 1]
    i = 0; rst = 0
    p1 = left; p2 = mid + 1; p = mid + 1
    while p1 <= mid:
         print("p1= "+str(p1))
         print("p: " +str(p)+"<= right:"+str(right)+" and "+str(nums[p1])+"/2.0 >"+ str(nums[p]))
         while (p <= right and (nums[p1] / 2.0) > nums[p]):
             p+=1
         rst += p - (mid + 1);
         while (p2 <= right and nums[p1] > nums[p2]):
             i+=1;p2+=1;p2+=1
             helper[i] = nums[p2]
         helper[i] = nums[p1]
    while (p2 <= right):
         i+=1
         p2+=1
         helper[i] = nums[p2]
    for i in range(0,len(helper)):
         nums[left + i] = helper[i]
    print("rst:"+str(rst))
    return 1;


reversePairs()