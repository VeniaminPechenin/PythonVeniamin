from random import*
def BelowAverage(numbers):
    average = sum(numbers) / len(numbers)
    for i in numbers:
        if i < average:
            print(i)
numbers = [randint(1,10) for i in range(10)]
print(numbers)
print(BelowAverage(numbers))
