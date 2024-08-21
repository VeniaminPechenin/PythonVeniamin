def SquareOfNumbers(numbers):
    summa = 0
    result = []
    for i in range(len(numbers)):
        summa += numbers[i] ** 2
        result += [str(numbers[i]) + '**2']
    result = ' + '.join(result)
    result += ' = ' + str(summa)
    return  result
numbers = [1,2,2,2,3]
print(SquareOfNumbers(numbers))