ones = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
        7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve',
        13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
        17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty',
        7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
millions = {1: 'Thousand', 2: 'Million', 3: 'Billion'}


def convertIntegerIntoWord(i):
    if i == 0:
        return 'zero'
    return getnumpos(i)


def getnumpos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return joinString(tens[i // 10], ones[i % 10])
    if i < 1000:
        return divItems(i, 100, 'Hundred')
    for inumber, iname in millions.items():
        if i < 1000**(inumber + 1):
            break
    return divItems(i, 1000**inumber, iname)


def divItems(position, inumber, iname):
    return joinString(
        getnumpos(position // inumber),iname,getnumpos(position % inumber),
    )


def joinString(*words):
    return ' '.join(filter(bool, words))


while True:
    try:
        (inputNumUser) = int(input('Please enter integer number: '))
        break
    except ValueError:
        print('Only integer numbers please!')
print(convertIntegerIntoWord(inputNumUser))