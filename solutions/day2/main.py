
def isWin(_a, _b):
    return (_a == 'A' and _b == 'Y') or (_a == 'B' and _b == 'Z') or (_a == 'C' and _b == 'X')


def isDraw(_a, _b):
    return (_a == 'A' and _b == 'X') or (_a == 'B' and _b == 'Y') or (_a == 'C' and _b == 'Z')


def get_input():
    with open('solutions/day2/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def getWinningAnswer(_a):
    if _a == 'A':
        return 'Y'
    if _a == 'B':
        return 'Z'
    if _a == 'C':
        return 'X'


def getLoosingAnswer(_a):
    if _a == 'A':
        return 'Z'
    if _a == 'B':
        return 'X'
    if _a == 'C':
        return 'Y'


def getDrawAnswer(_a):
    if _a == 'A':
        return 'X'
    if _a == 'B':
        return 'Y'
    if _a == 'C':
        return 'Z'


def task1():
    points = 0

    for line in get_input():
        a = line[0]
        b = line[2]

        if b == 'Z':
            points += 3
        elif b == 'Y':
            points += 2
        else:
            points += 1

        if isWin(a, b):
            points += 6
        elif isDraw(a, b):
            points += 3

    return points


def task2():
    points = 0
    for line in get_input():
        a = line[0]
        b = line[2]

        if b == 'X':
            answer_to_play = getLoosingAnswer(a)
        elif b == 'Y':
            answer_to_play = getDrawAnswer(a)
        else:
            answer_to_play = getWinningAnswer(a)

        if answer_to_play == 'Z':
            points += 3
        elif answer_to_play == 'Y':
            points += 2
        else:
            points += 1

        if b == 'Y':
            points += 3
        elif b == 'Z':
            points += 6

    return points
