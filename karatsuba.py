#!/usr/bin/env python3


def num_digits(num):
    return len(str(num))


def split_num(num, edge):
    snum = str(num)
    first = 0
    second = 0
    if snum[:edge]:
        first = int(snum[:edge])
    if snum[edge:]:
        second = int(snum[edge:])
    return first, second


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



def recursive_karatsuba(num1, num2, shift=''):

    shift = shift + "    "

    print(shift + '=============================')
    print(shift + 'num1 = ', num1)
    print(shift + 'num2 = ', num2)

    if num_digits(num1) == 2 or num_digits(num2) == 2:
        print(shift + 'res = ', num1 * num2)
        return num1 * num2

    n = max([num_digits(num1), num_digits(num2)])
    edge = n // 2
    (a, b) = split_num(num1, edge)
    (c, d) = split_num(num2, edge)

    print(shift + 'a = ', a)
    print(shift + 'b = ', b)
    print(shift + 'c = ', c)
    print(shift + 'd = ', d)

    ac = recursive_karatsuba(a, c, shift + 'ac: ')
    bd = recursive_karatsuba(b, d, shift + 'bd: ')
    sum_mul = recursive_karatsuba(a + b, c + d, shift + 'sm: ')

    return (10 ** num_digits(num1)) * ac + \
           (10 ** edge) * (sum_mul - ac - bd) + bd


#X = 21625695688898558125310188636840316594920403182768
#Y = 13306827740879180856696800391510469038934180115260
#RES = 287769407308846640970310151509826255482575362419155842891311909556878670000425352112987881085839680

X = 1234
Y = 5678
RES = 7006652

def test_karatsuba():
    assert karatsuba(X, Y) == RES


def test_recursive_karatsuba():
    assert recursive_karatsuba(X, Y) == RES