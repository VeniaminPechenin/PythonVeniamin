def IfPythonInString(string):
    for i in string:
        if "python" in string:
            return i
        #print(i)
string = ["python1","python12","qwdwn","cnoef"]
print(IfPythonInString(string))