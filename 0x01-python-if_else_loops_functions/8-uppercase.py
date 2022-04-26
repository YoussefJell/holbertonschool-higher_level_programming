#!/usr/bin/python3
def uppercase(str):
    newStr = ""
    for i in range(len(str)):
        ASCII = ord(str[i])
        if (ASCII >= 97 and ASCII <= 122):
            newStr += chr(ASCII - 32)
            continue
        newStr += str[i]
    print('{}'.format(newStr))
