#!/usr/bin/python3
# Converts a Roman numeral to an integer.

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    total = 0
    dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        val = dic[roman]
        total += val if total < val * 5 else -val
    return total
