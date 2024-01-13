from typing import List, Any

from InputReader import read_fixed_input
from itertools import groupby
from heapq import nlargest


def get_elfs_cargo(inp: list) -> list:
    return [sum(int(snack) for snack in cargo) for k, cargo in groupby(inp, key=lambda x: x != '') if k]


def part_one(inp: list) -> int:
    elfs = get_elfs_cargo(inp)
    return max(elfs)


def part_two(inp: list) -> int:
    elfs = get_elfs_cargo(inp)
    return sum(nlargest(3, elfs))


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    result_part_two = part_two(inp)
    print(f"Result for part one: {result_part_one}")
    print(f"Result for part two: {result_part_two}")


if __name__ == '__main__':
    main()
