#!/usr/bin/python3
def uppercase(str):
    """print a string in uppercase."""
    alp = list(str)
    for i in range(len(alp)):
        if (ord(alp[i]) > 96 and ord(alp[i]) < 123):
            alp[i] = chr(ord(alp[i]) - 32)
    print("{}".format("".join(alp)))
