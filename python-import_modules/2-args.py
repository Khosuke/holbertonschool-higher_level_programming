#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    str = "arguments:"
    j = 1
    args = sys.argv[1:]
    if len(args) == 1:
        str = "argument"
    if len(args) == 0:
        str = "arguments."
    print("{:d} {:s}".format(len(args), str))
    if len(args) != 0:
        for i in args:
            print("{:d}: {:s}".format(j, i))
            j += 1
