
stringWords = "hey fellow warriors"
stringWords = stringWords.split()
result = []
for i in stringWords:
    if len(i) > 5:
        result += [i[::-1]]
    else:
        result += [i]
result = " ".join(result)
print(result)






stringWords = "hey fellow warriors"
stringWords = stringWords.split()

for i in range(len(stringWords)):
    if len(stringWords[i]) > 5:
        stringWords[i] = stringWords[i][::-1]

print(' '.join(stringWords))