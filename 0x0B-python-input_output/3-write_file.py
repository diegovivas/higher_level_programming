#!/usr/bin/python3
def write_file(filename="", text=""):
    count = 0
    with open(filename, mode='w', encoding="utf-8") as file:
        count = file.write(text)
    return count
