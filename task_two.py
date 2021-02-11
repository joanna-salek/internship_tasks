#!/usr/bin/python
# -*- coding: UTF-8 -*-


def d_to_b(x):
    return bin(int(x)).replace("0b", "")


def b_to_d(x):
    return int(x, 2)


if __name__ == '__main__':
    while True:
        mode = input("If you want to convert decimal to binary choose 0 else binary to decimal press 1: ")
        if mode == "0":
            try:
                number = input("Please provide number in decimal mode: ")
                print(f"binary equivalent of decimal {number} is", d_to_b(number))
                break
            except ValueError:
                print("invalid number, try again")
        elif mode == "1":
            try:
                number = input("Please provide number in binary mode: ")
                print(f"decimal equivalent of binary {number} is", b_to_d(number))
                break
            except ValueError:
                print("invalid number, try again")
        else:
            print("invalid mode, try again")
