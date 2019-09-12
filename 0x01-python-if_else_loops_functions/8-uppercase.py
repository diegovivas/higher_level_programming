#!/usr/bin/python3
def uppercase(str):
    x = 0
    for x in range(len(str)):
        if ord(str[x]) in range(97, 123):
            y = ord(str[x])
            y = y - 32
        else:
            y = ord(str[x])

        print("{}".format(chr(y)), end='')
    print()
