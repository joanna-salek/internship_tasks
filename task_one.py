#!/usr/bin/python
# -*- coding: UTF-8 -*-

def byte_empty(byte):
    # check if bits contain only 0
    return True if byte.count("0") == 8 else False


def byte_validation(byte):
    # check if validation number (4 first bits, if last one is equal to 0 number is even, else odd)
    # match to identification number (even = 0 / odd = 1)
    return True if byte[3] == byte[7] else False


if __name__ == '__main__':
    # read and divide file into 8 digits bytes,
    # count errors and bytes
    # keep track of validate bytes in "v_objects" string
    with open("input.txt", "r", encoding="utf-8") as file:
        b = file.read(8)
        count_byte = 0
        count_errors = 0
        v_objects = ""
        while b:
            count_byte += 1
            if not byte_empty(b) and byte_validation(b):
                v_objects = v_objects + b
            else:
                count_errors += 1
            b = file.read(8)
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(f"{count_byte}\n{count_errors}\n{str(v_objects)}")

