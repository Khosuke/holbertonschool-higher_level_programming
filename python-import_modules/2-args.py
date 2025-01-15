#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    str = "arguments:"
    nb_arg = len(argv) - 1

    if nb_arg == 1:
        str = "argument:"
    if nb_arg == 0:
        str = "arguments."
    print("{:d} {:s}".format(nb_arg, str))
    if nb_arg > 0:
        for i in range (1, nb_arg + 1):
            print("{:d}: {:s}".format(i, argv[i]))
