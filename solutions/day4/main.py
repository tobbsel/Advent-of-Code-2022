
def get_example_input():
    s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    return s.splitlines()


def get_input():
    with open('solutions/day4/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]


def overlap(a, b):
    a_numbers = range(a[0], a[1] + 1)
    b_numbers = range(b[0], b[1] + 1)

    return len(set(a_numbers).intersection(b_numbers)) > 0


def task1():
    counter = 0
    for line in get_input():
        first_range, second_range = [[int(s) for s in elf_range.split('-')] for elf_range in line.split(',')]
        if contains(first_range, second_range) or contains(second_range, first_range):
            counter += 1
    return counter


def task2():
    counter = 0
    for line in get_input():
        first_range, second_range = [[int(s) for s in elf_range.split('-')] for elf_range in line.split(',')]
        if overlap(first_range, second_range):
            counter += 1
    return counter
