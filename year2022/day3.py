from InputReader import read_fixed_input

UPPERCASE_PRIORITY_SUBTRAHEND = 38
LOWERCASE_PRIORITY_SUBTRAHEND = 96


def part_one(inp: list) -> int:
    priority_sum = 0
    for rucksack in inp:
        left_side, right_side = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
        intersection = left_side.intersection(right_side)
        for item in intersection:
            if item.isupper():
                priority_sum += ord(item) - UPPERCASE_PRIORITY_SUBTRAHEND
            else:
                priority_sum += ord(item) - LOWERCASE_PRIORITY_SUBTRAHEND
    return priority_sum


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    print(f"Result for part one: {result_part_one}")


if __name__ == '__main__':
    main()
