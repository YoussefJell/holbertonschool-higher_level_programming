#!/usr/bin/python3
for x in range(0, 99):
    if x % 10 > x / 10:
        if x != 89:
            print(f"{x:02d}, ", end='')
        else:
            print(f"{x:02d}")
