#!/usr/bin/python3
def remove_char_at(str, n):
    """Creates a copy of the string, removing the character at the position"""
    if n >= 0:
        copystr = str[:n] + str[n + 1:]
        return (copystr)
    else:
        return (str)
