#!/usr/bin/python3
from calculator_1 import add, div, sub, mul
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    opers = {'+': add,
             '-': sub,
             '*': mul,
             '/': div}
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        for key in opers:
            if argv[2] == key:
                operfunc = opers.get(argv[2])
                print(f"{a} {argv[2]} {b} = {operfunc(a, b)}")
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
