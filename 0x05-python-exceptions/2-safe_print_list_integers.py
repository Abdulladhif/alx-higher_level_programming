#!/usr/bin/python3
# prints the first x elements of a list and only integers.


def safe_print_list_integers(my_list=[], x=0):
    try:
        elements = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            elements += 1
    except (TypeError, ValueError):
        pass
    print("")
    return (elements)
