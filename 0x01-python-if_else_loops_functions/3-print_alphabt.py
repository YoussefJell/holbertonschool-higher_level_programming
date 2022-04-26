#!/usr/bin/python3
for x in range(97, 97 + 26):
    if chr(x) != 'q' and chr(x) != 'e':
        print(f"{chr(x)}", end='')
