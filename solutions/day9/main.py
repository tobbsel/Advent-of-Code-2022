import numpy as np


movements = {
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
    'L': np.array([-1, 0]),
    'R': np.array([1, 0]),
}


def get_example_input1():
    s = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    return s.splitlines()


def get_example_input2():
    s = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    return s.splitlines()


def get_input():
    with open('solutions/day9/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def follow_previous_rope_part(head, tail):
    # only move tail, if head moves further than 1 tile aways

    def do_move(i, j):
        if abs(head[i] - tail[i]) > 1:
            tail[i] += np.sign(head[i] - tail[i])
            if head[j] != tail[j]:
                tail[j] += np.sign(head[j] - tail[j])
            return True
        return False

    if not do_move(0, 1):
        do_move(1, 0)


def move_rope(rope_length, input_data):
    directions_and_steps = [(line.split(' ')[0], int(line.split(' ')[1])) for line in input_data]
    rope_parts = [np.array([0, 0]) for _ in range(rope_length)]

    tail_positions_visited = []
    for direction, steps in directions_and_steps:
        for i in range(steps):
            rope_parts[0] += movements[direction]

            for j in range(1, rope_length):
                follow_previous_rope_part(rope_parts[j - 1], rope_parts[j])

            if str(rope_parts[-1]) not in tail_positions_visited:
                tail_positions_visited.append(str(rope_parts[-1]))

    return tail_positions_visited


def task1():
    input_data = get_input()
    tail_positions_visited = move_rope(2, input_data)
    return len(tail_positions_visited)


def task2():
    input_data = get_input()
    tail_positions_visited = move_rope(10, input_data)

    return len(tail_positions_visited)
