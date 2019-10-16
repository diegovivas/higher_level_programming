#!/usr/bin/python3
def append_write(filename="", text=""):
    count = 0
    with open(filename, mode='a', encoding="utf-8") as file:
        count = file.write(text)
    return count
