#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    from sys import argv
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == '+':
            res = add(a, b)
            print(f"{a} + {b} = {res}")
            exit(0)
        elif operator == '-':
            res = sub(a, b)
            print(f"{a} - {b} = {res}")
            exit(0)
        elif operator == '*':
            res = mul(a, b)
            print(f"{a} * {b} = {res}")
            exit(0)
        elif operator == '/':
            res = div(a, b)
            print(f"{a} / {b} = {res}")
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
