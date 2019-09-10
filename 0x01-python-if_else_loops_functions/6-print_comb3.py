#!/usr/bin/python3
for x in range(9):
    for y in range(10):
        if x < y and not (x == 8 and y == 9):
            print("{}{}".format((x), (y)), end=", ")
print(89)
