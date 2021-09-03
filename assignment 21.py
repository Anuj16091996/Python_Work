import random
import statistics

def median(array):
    if len(array) % 2 == 0:
        indexA = int(len(array) / 2)
        return (array[indexA] + array[indexA+1]) / 2
    else:
        indexB = int(len(array) / 2)
        return array[indexB]
nums1 = []
m = random.randint(0, 10)
i = 0
while i < m:
    nums1.append(random.randint(1, 10))
    i += 1
nums1.sort()
nums2 = []
n = random.randint(0, 10)
i = 0
while i < n:
    nums2.append(random.randint(1, 10))
    i += 1
nums2.sort()
combined = []
for n in nums1:
    combined.append(n)
for n in nums2:
    combined.append(n)
combined.sort()
print('Input: nums1 = {0}, nums2 = {1}'.format(nums1,nums2))
print('Output: {0}'.format(median(combined)))
