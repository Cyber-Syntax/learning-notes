# TODO Ask AI to understand more clearly

def getStr(s):
    c = [char for char in s]
    new_word  = "".join([char * 3 for char in c])
    return new_word

print(getStr("abc"))

def getStr(s):
    return "".join([char * 3 for char in s])

print(getStr("xyz"))

def convert_string(str):
    new_str = ""
    for char in str:
        new_str = new_str + char * 3
    return new_str

print(convert_string("def"))
