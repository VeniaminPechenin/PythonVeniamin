def Accum(word):
    word = list(word)
    for i in range(len(word)):
        word[i] = word[i].upper()
        word[i] += word[i].lower() * i
    word = '-'.join(word)
    return print(word)

Accum("abс")