#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        val = ord(str[i])
        if val >= 97 and val <= 122:
            val -= 32
            print(f"{chr(val)}", end='')
        else:
            print(f"{chr(val)}", end='')
        i += 1
    print()
