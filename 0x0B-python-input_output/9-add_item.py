#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == '__main__':

    try:
        filename = "add_item.json"
        my_list = load_from_json_file(filename)
    except Exception:
        filename = "add_item.json"
        my_list = []
        save_to_json_file(my_list, filename)
    x = len(sys.argv)
    y = 1
    while(y < x):
        my_list.append(sys.argv[y])
        y += 1
    save_to_json_file(my_list, filename)
