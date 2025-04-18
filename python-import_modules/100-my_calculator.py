#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators_list = ["+", "-", "*", "/"]
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator not in operators_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            result = div(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
