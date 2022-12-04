#!/usr/bin/python3
"""Deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    if idx >= 0 and len(my_list) > 0:
        del my_list[idx]
    return my_list
