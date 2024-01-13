from InputReader import read_fixed_input
from itertools import groupby


def part_one(inp: list) -> int:
    elfs = [sum(int(snack) for snack in cargo) for k, cargo in groupby(inp, key=lambda x: x != '') if k]
    return max(elfs)


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    print(f"Result for part one: {result_part_one}")


if __name__ == '__main__':
    main()
