def CamelCase(stringOfWords):
    stringOfWords = stringOfWords.replace("-"," ").replace("_"," ").split()
    for i in range(1,len(stringOfWords)):
        stringOfWords[i] = stringOfWords[i].capitalize()
    print("".join(stringOfWords))
string = "qwerty-qwerty1_qwerty3"
CamelCase(string)
