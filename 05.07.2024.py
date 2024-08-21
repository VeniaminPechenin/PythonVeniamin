def Palindrome(number):
    numberStr = str(number)
    for i in range(len(numberStr) // 2):
        if numberStr[i] != numberStr[len(numberStr) - 1 - i]:
            return False
    return True
def PrintPslindrome(numbers):
    for j in numbers:
        if Palindrome(j):
            print(j)
numbers = [12321, 54345, 67876, 12345, 98789, 555, 434]
print(PrintPslindrome(numbers))
PrintPslindrome