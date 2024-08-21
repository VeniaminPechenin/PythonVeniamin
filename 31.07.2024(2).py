def MathematicalOperation(numbers):
    if numbers[0] == "+":
        result = numbers[1]  + numbers[2]
    if numbers[0] == "-":
        result = numbers[1] - numbers[2]
    if numbers[0] == "/":
        result = numbers[1] / numbers[2]
    if numbers[0] == "*":
        result = numbers[1] * numbers[2]
    return result
task = ["*",1,2]
print(MathematicalOperation(task))