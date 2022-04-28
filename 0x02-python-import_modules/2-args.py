#!/usr/bin/python3
from sys import argv
argc = len(argv)
i = 1
if argc == 1:
    print("0 arguments.")
elif argc == 2:
    print("1 argument:")
    print("1: {}".format(argv[1]))
else:
    print("{} arguments:".format(argc - 1))
    while i < argc:
        print("{}: {}".format(i, argv[i]))
        i += 1
