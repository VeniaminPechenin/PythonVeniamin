def FirstWord(string):

    for i in string:
        first_word = i.split()[0]
        print(first_word)
string= ["qwert trhthrh", "sdfv fdsv", "asdf gdb"]
print(FirstWord(string))