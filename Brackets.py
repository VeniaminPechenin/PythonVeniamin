def FirstCheck(string):
    if len(string) % 2 == 0:
        return True


def SecondCheck(string):
    for i in range(0,len(string) - 1, 2):
        staple = ["[]","()","{}"]
        result = string[i] + string[i + 1]
        if result in staple:
            continue
        else:
            return False
    return True


def ThirdCheck(string):
    firstStringStaple = string[:len(string) // 2]
    secondStringStaple = string[len(string) // 2:]
    for i in range(len(string)):
        resultSumma = (firstStringStaple[len(firstStringStaple) - i - 1]
                      + secondStringStaple[i])
        if resultSumma == '()' or resultSumma == '[]' or resultSumma == '{}':
            continue
        else:
            return False
            break
    return True


stringStaple = "[({})]](]"
print(ThirdCheck(stringStaple))