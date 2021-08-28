import random


def checkPosition(row, col, groupNumber):
    checkedPositions.append([row, col])
    if row > 0:
        if nGrid[(row - 1)][col] > 0 and positionReviewed((row - 1), col):
            if nGrid[row][col] == 1:
                nGrid[row][col] = groupNumber
                nGrid[(row - 1)][col] = nGrid[row][col]
                groupNumber = groupNumber + 1
            else:
                nGrid[(row - 1)][col] = nGrid[row][col]
            checkPosition((row - 1), col, groupNumber)
    if col > 0:
        if nGrid[row][(col - 1)] > 0 and positionReviewed(row, (col - 1)):
            if nGrid[row][col] == 1:
                nGrid[row][col] = groupNumber
                nGrid[row][(col - 1)] = nGrid[row][col]
                groupNumber = groupNumber + 1
            else:
                nGrid[row][(col - 1)] = nGrid[row][col]
            checkPosition(row, (col - 1), groupNumber)
    if row < (m - 1):
        if nGrid[(row + 1)][col] > 0 and positionReviewed((row + 1), col):
            if nGrid[row][col] == 1:
                nGrid[row][col] = groupNumber
                nGrid[(row + 1)][col] = nGrid[row][col]
                groupNumber = groupNumber + 1
            else:
                nGrid[(row + 1)][col] = nGrid[row][col]
            checkPosition((row + 1), col, groupNumber)
    if col < (n - 1):
        if nGrid[row][(col + 1)] > 0 and positionReviewed(row, (col + 1)):
            if nGrid[row][col] == 1:
                nGrid[row][col] = groupNumber
                nGrid[row][(col + 1)] = nGrid[row][col]
                groupNumber = groupNumber + 1
            else:
                nGrid[row][(col + 1)] = nGrid[row][col]
            checkPosition(row, (col + 1), groupNumber)
    return groupNumber


def positionReviewed(row1, col1):
    for position in checkedPositions:
        if [row1, col1] == position:
            return False
    return True


m = random.randint(1, 10)
n = random.randint(1, 10)
checkedPositions = [[10, 10]]
nGrid = []
line = 0
print('Input:')
print('rows = ' + str(m))
print('columns = ' + str(n))
print('grid =')
while line < m:
    column = 0
    toAdd = []
    while column < n:
        toAdd.append(random.randint(0, 1))
        column = column + 1
    nGrid.append(toAdd)
    line = line + 1

line = 0
while line < m:
    column = 0
    toPrint = ''
    while column < n:
        toPrint = toPrint + '\t' + str(nGrid[line][column])
        column = column + 1
    print(toPrint)
    line = line + 1

groupNumber = 2
line = 0
while line < m:
    column = 0
    while column < n:
        if (nGrid[line][column] != 0) and positionReviewed(line, column):
            groupNumber = checkPosition(line, column, groupNumber)
        column = column + 1
    line = line + 1

# print("\nGrouped matrix")
#
# line = 0
# while line < m:
#     column = 0
#     toPrint = ''
#     while column < n:
#         toPrint = toPrint + '\t' + str(nGrid[line][column])
#         column = column + 1
#     print(toPrint)
#     line = line + 1

setOfGroups = set()
line = 0
while line < m:
    column = 0
    while column < n:
        if nGrid[line][column] > 1:
            setOfGroups.add(nGrid[line][column])
        column = column + 1
    line = line + 1

print('\nOutput: ' + str(len(setOfGroups)))
