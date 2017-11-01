#!/usr/bin/env python3

class MinMaxStack:
    def __init__(self):
        self.items = []
        self.minmax = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

        if self.minmax:
            cur_min, cur_max = self.minmax[len(self.minmax) - 1]
            new_min = min(cur_min, item)
            new_max = max(cur_max, item)
        else:
            new_min = new_max = item

        self.minmax.append((new_min, new_max))

    def pop(self):
        self.minmax.pop()
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def get_min(self):
        return self.minmax[len(self.minmax) - 1][0]

    def get_max(self):
        return self.minmax[len(self.minmax) - 1][1]

    def size(self):
        return len(self.items)


def test_min():
    s = MinMaxStack()
    s.push(1)
    s.push(2)
    s.push(10)
    s.push(5)

    assert s.get_min() == 1


def test_max():
    s = MinMaxStack()
    s.push(1)
    s.push(2)
    s.push(10)
    s.push(5)

    assert s.get_max() == 10