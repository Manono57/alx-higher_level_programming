#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_digits[roman_string[j]] > roman_digits[roman_string[j - 1]]:
            roman_number += roman_digits[roman_string[j]] - 2 * \
                        roman_digits[roman_string[j - 1]]
        else:
            roman_number += roman_digits[roman_string[j]]
    return roman_number
