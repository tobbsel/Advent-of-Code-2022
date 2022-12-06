import re
from typing import List


def get_example_input():
    s = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    return s.splitlines()


def get_initial_state(input_data: List[str]):
    empty_line_index = input_data.index('')
    state_data = input_data[:empty_line_index-1]
    indices = input_data[empty_line_index-1]
    row_length = len(state_data[-1])

    stacks = [[] for _ in indices.split('   ')]
    for row in state_data[::-1]:
        crates = ("{:<" + str(row_length) + "}").format(row)
        # print(crates)
        crates = crates\
            .replace('    [', '[ ] [')\
            .replace('    ', ' [ ]')\
            .lstrip('[')\
            .rstrip(']')\
            .split('] [')

        for i, stack in enumerate(stacks):
            if crates[i] != ' ':
                stack.append(crates[i])

    return stacks


def get_input():
    with open('solutions/day5/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def process_stacks(stacks, moves, do_move):
    for move in moves:
        do_move(stacks, move)

    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])


def process_input(input_data):
    stacks = get_initial_state(input_data)
    empty_line_index = input_data.index('')
    moves = [(int(num) for num in re.findall(r'\d+', line)) for line in input_data[empty_line_index+1:]]

    return stacks, moves


def task1():
    input_data = get_input()
    stacks, moves = process_input(input_data)

    def move_1_by_1(_stacks, move):
        count, source, dest = move
        for _ in range(count):
            crate = stacks[source - 1].pop()
            stacks[dest - 1].append(crate)

    return process_stacks(stacks, moves, move_1_by_1)


def task2():
    input_data = get_input()
    stacks, moves = process_input(input_data)

    def move_stacked(_stacks, move):
        count, source, dest = move

        crates = stacks[source - 1][-count:]
        del stacks[source - 1][-count:]
        stacks[dest - 1] += crates

    return process_stacks(stacks, moves, move_stacked)
