def BinaryToDecimal(n):
    num=n
    dec_value=0
    base=1

    temp=num
    while temp>0:
        last_digit=temp%10
        temp=int(temp/10)

        dec_value=dec_value+last_digit * base
        base=base*2

    return dec_value



Num=100001
print(BinaryToDecimal(Num))

