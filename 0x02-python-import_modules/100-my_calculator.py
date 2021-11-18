#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arg_len = len(argv) - 1

    if arg_len == 3:

        a = int(argv[1])
        b = int(argv[3])
        opp = argv[2]

        if opp == "+":
            sum = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, sum))
        elif opp == "-":
            sum = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, sum))
        elif opp == "*":
            sum = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, sum))
        elif opp == "/":
            sum = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, sum))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
