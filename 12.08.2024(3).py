def FirstUniqueSymbol(stringOfWords):
    for i in range(len(stringOfWords)):
        result = stringOfWords.count(stringOfWords[i])
        if result == 1:
            return print(stringOfWords[i])
string = "accdc"
FirstUniqueSymbol(string)