bills = [[124, 48, 268, 180, 42], [77, 375, 110, 45]]
tip = [[0.20, 0.15, 0.10], [0.20, 0.10, 0.25]]
limitBill = [[50, 200], [100, 300]]

def avarageBill(bill):
    average = sum(bill)/len(bill)
    print("The bill's average is: " + str(average))

class Calculator:
    def calculateTip(bill, tipValue, limit):
        tipBill = []
        finalAmount = []
        for i in range(0, len(bill)):
            if bill[i] <= limit[0]:
                tipBill.append(round(bill[i] * tipValue[0], 2))
                finalAmount.append(bill[i] + tipBill[i])
            elif bill[i] > limit[0] and bill[i] <= limit[1]:
                tipBill.append(round(bill[i] * tipValue[1], 2))
                finalAmount.append(bill[i] + + tipBill[i])
            else:
                tipBill.append(round(bill[i] * tipValue[2], 2))
                finalAmount.append(bill[i] + + tipBill[i])
        print('Bills value: ' + str(bill))
        print('Tips value: ' + str(tipBill))
        print('Final amounts value: ' + str(finalAmount))


print("The value for the John's familly are: ")
Calculator.calculateTip(bills[0], tip[0], limitBill[0])
avarageBill(bills[0])
print("\nThe value for the Mark's familly are: ")
Calculator.calculateTip(bills[1], tip[1], limitBill[1])
avarageBill(bills[1])