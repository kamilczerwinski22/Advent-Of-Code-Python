from InputReader import read_fixed_input
from typing import Iterable

UPPERCASE_PRIORITY_SUBTRAHEND = 38
LOWERCASE_PRIORITY_SUBTRAHEND = 96


def chunk(lst: list, n: int) -> list[set]:
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_priority_sum(lst: Iterable) -> int:
    priority_sum = 0
    for item in lst:
        if item.isupper():
            priority_sum += ord(item) - UPPERCASE_PRIORITY_SUBTRAHEND
        else:
            priority_sum += ord(item) - LOWERCASE_PRIORITY_SUBTRAHEND
    return priority_sum


def part_one(inp: list) -> int:
    priority_sum = 0
    for rucksack in inp:
        left_side, right_side = set(rucksack[:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:])
        priority_sum += get_priority_sum(left_side.intersection(right_side))
    return priority_sum


def part_two(inp: list) -> int:
    priority_sum = 0
    for group in chunk(inp, 3):
        priority_batch = set.intersection(*(set(element) for element in group))
        priority_sum += get_priority_sum(priority_batch)
    return priority_sum


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    result_part_two = part_two(inp)
    print(f"Result for part one: {result_part_one}")
    print(f"Result for part one: {result_part_two}")


if __name__ == '__main__':
    main()
