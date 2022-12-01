#!/usr/bin/python3
""" Pints all the names defined by the compiled module file"""
if __name__ == "__main__":
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] != "__": # not start with __
            print(name)
