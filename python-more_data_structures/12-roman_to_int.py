def roman_to_int(roman_string):
	dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	result = 0
	len_string = len(roman_string)
	for i in range(len_string):
		if i + 1 < len_string and dict_roman[roman_string[i]] < dict_roman[roman_string[i + 1]]:
			result -= dict_roman[roman_string[i]]
		else:
			result += dict_roman[roman_string[i]]
	return result
