#!/usr/bin/python3
# Adds all unique integers in a list (only once for each integer).

def uniq_add(my_list=[]):
    total = 0
    for i in set(my_list):
        total += i
    return total
