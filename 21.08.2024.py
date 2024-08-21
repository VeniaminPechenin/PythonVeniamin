from random import*
def TwoMaxNUmbers(listNumbers):
    listNumbers = sorted(listNumbers)
    summa = listNumbers[-2] + listNumbers[-1]
    print(listNumbers)
    print(summa)
listNumbers = [randint(1,100) for i in range(5)]
TwoMaxNUmbers(listNumbers)