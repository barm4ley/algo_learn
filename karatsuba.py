#!/usr/bin/env python3


def num_digits(num):
    return len(str(num))


def split_num(num, edge):
    snum = str(num)
    return int(snum[:edge]), int(snum[edge:])


def karatsuba(num1, num2):
    if num_digits(num1) < 10 or num_digits(num2) < 10:
        return num1 * num2

    n = max([num_digits(num1), num_digits(num2)])
    edge = n // 2
    (a, b) = split_num(num1, edge)
    (c, d) = split_num(num2, edge)

    ac = a * c
    bd = b * d

    return (10 ** num_digits(num1)) * ac + \
           (10 ** edge) * ((a + b) * (c + d) - ac - bd) + bd

def test_karatsuba():
    x = 21625695688898558125310188636840316594920403182768
    y = 13306827740879180856696800391510469038934180115260
    res = karatsuba(x, y)

    known_result = 287769407308846640970310151509826255482575362419155842891311909556878670000425352112987881085839680

    assert res == known_result