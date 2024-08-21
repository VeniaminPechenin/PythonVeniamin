def ArrayInversion(startArray,endArray):
    newArray = []
    for i in range(len(startArray)):
        if startArray[i] not in endArray:
            newArray.append(startArray[i])
    return print(newArray)

startArray = [1,2,3,4,5]
endArray = [1,2]
ArrayInversion(startArray,endArray)
