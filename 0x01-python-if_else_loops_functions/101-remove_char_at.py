#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = str
    if n >= 0:
        newStr = newStr[:n] + newStr[n+1:]
    return newStr
