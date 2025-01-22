def roman_to_int(roman_string):
    rNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    l_str = len(roman_string)
    for i in range(l_str):
        if i + 1 < l_str and rNum[roman_string[i]] < rNum[roman_string[i + 1]]:
            result -= rNum[roman_string[i]]
        else:
            result += rNum[roman_string[i]]
    return result
