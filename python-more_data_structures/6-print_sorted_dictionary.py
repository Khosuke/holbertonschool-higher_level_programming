#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key_s in sorted(a_dictionary):
        print("{}: {}".format(key_s, a_dictionary[key_s]))
