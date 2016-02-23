#!/usr/bin/env python3


def num_digits(num):
    return len(str(num))

def split_num(num, edge):
    snum = str(num)
    return int(snum[:edge]), int(snum[edge:])

def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2


    edge = max([num_digits(num1), num_digits(num2)]) // 2
    (a, b) = split_num(num1, edge)
    (c, d) = split_num(num2, edge)

