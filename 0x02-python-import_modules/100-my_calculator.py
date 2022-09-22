#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operatorerator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    from sys import argv
    arg_calc(argv)
