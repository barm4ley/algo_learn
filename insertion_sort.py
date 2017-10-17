#!/usr/bin/env python3


def sort(lst):
    for i in range(1, len(lst)):
        val = lst.pop(i)
        j = i - 1

        while j >= 0 and val < lst[j]:
            j -= 1

        lst.insert(j + 1, val)
    return lst



SORTED = [1, 2, 3, 4, 5]

def test_inversed():
    assert sort([5,4,3,2,1]) == SORTED

def test_presorted():
    assert sort(SORTED) == SORTED

def test_random():
    assert sort([1,4,5,3,2]) == SORTED