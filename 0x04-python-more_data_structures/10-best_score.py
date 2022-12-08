#!/usr/bin/python3
# Returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_val = max(a_dictionary, key= lambda val: a_dictionary[val])
    return max_val
