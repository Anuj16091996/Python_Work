def OddNumberProduct():
    product=1
    for j in range(1,16):
        if(j%2==1):
            product=j*product
    return product


def Main():
    print(OddNumberProduct())

Main()

