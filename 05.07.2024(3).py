def PowerOfTwo(numbers):
    for number in numbers:
        if number > 0 and (number & (number - 1)) == 0:
           print(number)
numbers = [2, 4, 6, 8, 10, 7 ]
PowerOfTwo(numbers)


