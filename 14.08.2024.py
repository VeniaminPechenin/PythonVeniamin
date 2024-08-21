def TwoStrings(defaultString,endString):
    if endString in defaultString:
        return  True
    else:
        return False
defaultString = "1234"
endString = "134"
print(TwoStrings(defaultString,endString))