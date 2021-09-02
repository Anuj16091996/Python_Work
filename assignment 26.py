import random

n = random.randint(0, 109)
rangeOfN = range(n + 1)
count = 0
for number in rangeOfN:
    count = count + str(number).count('1')
print('Input: n = ' + str(n))
print('Output: ' + str(count))
