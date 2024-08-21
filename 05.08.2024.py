def UniqueNumbers(numbers):
    for i in range(len(numbers)):
        result = numbers.count(numbers[i])
        if result == 1:
            return numbers[i]

numbers = [4,5,4,4]
print(UniqueNumbers(numbers))