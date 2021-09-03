import random

height = []
i = 0
while i < random.randint(1, (2 * 104)):
    height.append(random.randint(0, 105))
    i += 1

for number in height:
    rangeOfNumbers = range(number)
    toAdd = []
    for n in rangeOfNumbers:
        toAdd.append(n + 1)
    rowLine = ''
    for n in toAdd:
        rowLine = rowLine + str(n) + ' '
    print(rowLine)

left = 0
right = len(height) - 1
water = 0
left_max = 0
right_max = 0
while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water = water + (left_max - height[left])
        left = left + 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water = water + (right_max - height[right])
        right = right - 1
print(water)
