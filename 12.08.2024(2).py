def NumderOfvowels(stringOfWords):
    vowels = "aioue"
    count = 0
    for i in range(len(stringOfWords)):
        if stringOfWords[i] in vowels:
            count += 1
    print(count)
stringOfWords = "aicmdu"
NumderOfvowels(stringOfWords)






