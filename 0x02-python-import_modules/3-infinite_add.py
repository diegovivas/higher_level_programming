#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    if len(sys.argv) == 1:
        print('0')
    else:
        for x in range(len(sys.argv)):
            if x > 0:
                suma = suma + int(sys.argv[x])

        print('{}'.format(suma))
