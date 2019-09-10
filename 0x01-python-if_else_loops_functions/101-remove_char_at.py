#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for x in range(len(str)):
        if x != n:
            str2 = str2 + str[x]
    return str2
