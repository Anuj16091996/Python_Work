while True:
    try:
        numRouters = int(input("Please the number of routers in the data center (>=3): "))
        while numRouters < 3:
            numRouters = int(input("Please enter a correct number of routers greater than 2: "))
        while True:
            try:
                numLinks = int(input("Please enter a links' numbers: "))
                break
            except ValueError:
                print('Please enter only numbers')
        break
    except ValueError:
        print('Please enter only numbers')

def numMaxRoutes(num):
    while True:
        try:
            while num > numRouters:
                num = int(input('Please enter a number less than ' + str(numRouters) + ': '))
            break
        except ValueError:
            print('Please enter only numbers')
    return num

links = []
for i in range(1, numLinks +1):
    first = numMaxRoutes(int(input("Link {0}: enter a 1er Route: ".format(i))))
    second = numMaxRoutes(int(input("Link {0}: enter a 2nd Route: ".format(i))))
    link = [first, second]
    links.append(link)

print(links)
impRouters = []

def includes(arr, value):
    for i in arr:
        if i == value:
            return True
    return False

def failrouter(links, router):
    temp=[]
    for link in links:
        if not includes(link, router):
            temp.append(link)
    return temp

def isRouterMissing(links, numRouters, curr):
    contains = False
    for i in range(1, numRouters+1):
        if i == curr:
            continue
        for j in range(0, len(links)):
            if includes(links[j], i):
                contains = True
                break
            contains = False
        if not contains:
            break
    return contains

def isConnected(temp):
    for i in range(0, len(temp)):
        tempRouter1 = temp[i][0]
        tempRouter2 = temp[i][1]
        connFound = False

        for j in range(0, len(temp)):
            if i == j:
                continue

            if includes(temp[j], tempRouter1) or includes(temp[j], tempRouter2):
                connFound = True
                break

        if not connFound:
            return True
    return False


for i in range(1, numRouters+1):
    temp = failrouter(links, i)
    if isRouterMissing(temp, numRouters, i):
        impRouters.append(isConnected(temp))
    else:
        impRouters.append(True)

for idx, val in enumerate(impRouters):
    if val:
        print(idx+1)
