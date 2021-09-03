def limitString(text):
    while True:
        try:
            while len(text) <= 0 or len(text) >= 10:
                text = (input('Error: your variable (in lowercase) between 0 to 2000 characters: '))
        except ValueError:
            print('The string is outside of range: 0 to 2000 characters')
        return text

def isEnglish(t):
    while True:
        try:
            while t.encode(encoding='utf-8').decode('ascii'):
                return t
        except ValueError:
            t = (input('Error: only English letters, try again: '))

def isMatching(s, p, n, m, lookup):
    if m < 0 and n < 0:
        return True

    elif m < 0:
        return False

    elif n < 0:
        for i in range(m + 1):
            if p[i] != '*':
                return False
        return True

    if not lookup[n][m]:
        if p[m] == '*':
            lookup[n][m] = isMatching(s, p, n - 1, m, lookup) or \
                           isMatching(s, p, n, m - 1, lookup)
        else:
            if p[m] != '?' and p[m] != s[n]:
                lookup[n][m] = False
            else:
                lookup[n][m] = isMatching(s, p, n - 1, m - 1, lookup)
    return lookup[n][m]

s = isEnglish(limitString((input("S: enter your variable (in lowercase): ")).lower()))
p = isEnglish(limitString((input("P: enter your variable (in lowercase): ")).lower()))

lookup = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]

if isMatching(s, p, len(s) - 1, len(p) - 1, lookup):
    print('Output: ', True)
else:
    print('Output: ', False)
