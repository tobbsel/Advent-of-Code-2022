import numpy as np


def get_example_input():
    s = """30373
25512
65332
33549
35390"""
    return s.splitlines()


def get_input():
    with open('solutions/day8/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def task1():
    input_data = get_input()
    trees = np.array([[int(char) for char in line] for line in input_data], dtype=int)

    visible_count = 0
    for i in range(1, trees.shape[0] - 1):
        for j in range(1, trees.shape[1] - 1):
            if trees[i, j] > np.max(trees[:i, j]) \
                    or trees[i, j] > np.max(trees[i+1:, j]) \
                    or trees[i, j] > np.max(trees[i, :j]) \
                    or trees[i, j] > np.max(trees[i, j+1:]):
                visible_count += 1

    visible_count += 2 * trees.shape[0] + 2 * trees.shape[1] - 4

    return visible_count


def task2():
    input_data = get_input()
    trees = np.array([[int(char) for char in line] for line in input_data], dtype=int)

    max_score = 0
    for i in range(1, trees.shape[0] - 1):
        for j in range(1, trees.shape[1] - 1):
            # I really dislike the following repetitions, but I am far to lazy to generalize this...

            count_left = 0
            for _i in range(i - 1, -1, -1):
                count_left += 1
                if trees[_i, j] >= trees[i, j]:
                    break

            count_right = 0
            for _i in range(i + 1, trees.shape[0]):
                count_right += 1
                if trees[_i, j] >= trees[i, j]:
                    break

            count_up = 0
            for _j in range(j - 1, -1, -1):
                count_up += 1
                if trees[i, _j] >= trees[i, j]:
                    break

            count_down = 0
            for _j in range(j + 1, trees.shape[1]):
                count_down += 1
                if trees[i, _j] >= trees[i, j]:
                    break

            score = count_left * count_right * count_up * count_down
            max_score = max(score, max_score)

    return max_score
