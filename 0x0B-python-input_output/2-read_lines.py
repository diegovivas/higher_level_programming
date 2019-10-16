#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, mode='r', encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        for line in file:
            count += 1
            if count <= nb_lines:
                print(line, end="")
    return count
