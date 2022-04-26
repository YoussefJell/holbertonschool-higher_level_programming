#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    lastDigit = number % 10
    print("{}".format(lastDigit), end='')
    return(lastDigit)
