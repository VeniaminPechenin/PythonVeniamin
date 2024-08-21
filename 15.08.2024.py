def ReplaceWords(string):
    string = string.split(" ")
    string = string[::-1]
    string = " ".join(string)
    return string
string = "Hello World qwerty"
print(ReplaceWords(string))


