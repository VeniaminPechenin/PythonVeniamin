from random import*
def UniqueElements(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList
list = [randint(1,10) for i in range(10)]
print(list)
uniqueList = UniqueElements(list)
print(UniqueElements(list))

