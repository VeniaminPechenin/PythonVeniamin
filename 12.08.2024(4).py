def QuantityOfUniqueNumbers(string):
    count = 0
    for i in range(len(string)):
        result = string.count(string[i])
        if result > 1:
            return print(result)
string = "aaad"
QuantityOfUniqueNumbers(string)