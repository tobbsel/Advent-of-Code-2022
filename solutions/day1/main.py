import os

def get_example_input():
    s = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    return s.splitlines()

def get_input():
    with open('solutions/day1/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def get_loads_sorted():
    loads = []
    buffer = 0
    for line in get_input():
        if line == '':
            loads.append(buffer)
            buffer = 0
        else:
            buffer += int(line.strip('\n'))

    return sorted(loads)

def task1():
    return get_loads_sorted()[-1]

def task2():
    return sum(get_loads_sorted()[-3:])
