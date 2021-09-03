import sys


def reversePairs(nums):
    res = mergesort(nums, 0, len(nums) - 1);
    return res;


def mergesort(nums, start, end):
    if start >= end:
        return 0
    mid = (end - start) / 2 + start;
    res = mergesort(nums, start, mid) + mergesort(nums, mid + 1, end)
    for i in range(start,mid):
        j = mid + 1
        while (j <= end and nums[i] / 2.0 > nums[j]):
            j +=1
        res += j - mid - 1
    merge(nums, start, mid, mid + 1, end)
    return res


def merge(nums, s1, e1, s2, e2):
    result = [e2 - s1 + 1];
    i = s1, j = s2, k = 0;
    while (i <= e1 or j <= e2):
        a = sys.maxsize
        b = sys.maxsize
        if (i <= e1):
            a = nums[i]
        if (j <= e2):
            b = nums[j]
        if (a < b):
            k+=1
            result[k] = a
            i +=1
        elif a > b:
            k+=1
            result[k] = b
            j +=1
        else:
            if j == e2 + 1 :
                k+=1
                result[k] = a
                i +=1
            else:
                k+=1
                result[k] = b
                j +=1
    for k in range(0, len(result)):
        nums[s1 + k] = result[k]

nums=[[1,3,2,3,1]]
reversePairs(nums)