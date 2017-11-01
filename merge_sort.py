#!/usr/bin/env python3




def sort(lst):
    print(lst)
    #if start < end:
    if len(lst) > 1:
        middle = len(lst) // 2
        left = sort(lst[:middle])
        right = sort(lst[middle:])
        return _merge(left, right)
    else:
        return _merge(lst, [])

def _merge(left, right):
    res = []
    l = r = 0
    while l < len(left) or r < len(right):

        # Left part is fully processed
        # Append right part to result
        if l >= len(left):
            res += right[r:]
            return res

        # Rigit part is processed
        # Append left part to result
        if r >= len(right):
            res += left[l:]
            return res

        # Check which suits condition and increment pointer
        if left[l] > right[r]:
            res.append(right[r])
            r += 1
        else:
            res.append(left[l])
            l += 1

    return res







SORTED = [1, 2, 3, 4, 5]


def test_inversed():
    lst = [5,4,3,2,1]
    assert sort(lst) == SORTED


def test_presorted():
    assert sort(SORTED) == SORTED


def test_random():
    lst = [1,4,5,3,2]
    assert sort(lst) == SORTED