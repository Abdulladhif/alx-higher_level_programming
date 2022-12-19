#!/usr/bin/python3
# prints x elements of a list


def safe_print_list(my_list=[], x=0):
    try:
        elements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            elements += 1
    except IndexError:
        pass
    print("")
    return (elements)
