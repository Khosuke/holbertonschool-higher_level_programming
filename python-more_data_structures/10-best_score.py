#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value_s = list(a_dictionary.values())
    key_s = list(a_dictionary.keys())
    biggest_value = value_s[0]
    for i in range(len(value_s)):
        if biggest_value < value_s[i]:
            biggest_value = value_s[i]
        else:
            continue
    return key_s[value_s.index(biggest_value)]

# alternative function to do the same but with shorter code
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
