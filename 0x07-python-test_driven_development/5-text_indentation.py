#!/usr/bin/python3
def text_indentation(text):
    flag = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for x in text:
        if x == "." or x == ":" or x == "?":
            print(x)
            flag = 1
        elif x == " " and flag == 1:
            flag = 0
        else:
            print(x, end="")

