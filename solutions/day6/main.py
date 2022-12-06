
def get_example_input():
    s = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
    return s.splitlines()


def get_input():
    with open('solutions/day6/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def distinct_of_length(buffer, n):
    for i in range(len(buffer)):
        if len(set(buffer[i:i+n])) == n:
            return i + n


def task1():
    buffer = get_input()[0]
    return distinct_of_length(buffer, 4)


def task2():
    buffer = get_input()[0]
    return distinct_of_length(buffer, 14)
