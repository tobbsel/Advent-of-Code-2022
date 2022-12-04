
def get_example_input():
    s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    return s.splitlines()


def get_input():
    with open('solutions/day3/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def getPrio(item: str) -> int:
    ascii_code = ord(item)
    if ascii_code - 64 <= 26:
        return ascii_code - 64 + 26
    else:
        return ascii_code - 96


def task1():
    prio_sum = 0
    for rucksack in get_input():
        middle_index = len(rucksack) // 2
        compartment1 = rucksack[:middle_index]
        compartment2 = rucksack[middle_index:]
        double_items = set(compartment1).intersection(compartment2)

        prio_sum += getPrio(next(iter(double_items)))

    return prio_sum


def task2():
    rucksacks = get_input()

    batch_prio_sum = 0
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i + 3]

        batch_item = next(iter(set(group[0]).intersection(group[1]).intersection(group[2])))

        batch_prio_sum += getPrio(batch_item)

    return batch_prio_sum
