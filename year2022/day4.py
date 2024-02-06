from InputReader import read_fixed_input


def is_fully_contained(first_elf_range: str, second_elf_range: str) -> bool:
    first_elf_start, first_elf_stop = map(int, first_elf_range.split('-'))
    second_elf_start, second_elf_stop = map(int, second_elf_range.split('-'))

    return (first_elf_start <= second_elf_start and first_elf_stop >= second_elf_stop) or \
           (second_elf_start <= first_elf_start and second_elf_stop >= first_elf_stop)


def ranges_overlap(first_elf_range: str, second_elf_range: str) -> bool:
    first_elf_start, first_elf_stop = map(int, first_elf_range.split('-'))
    second_elf_start, second_elf_stop = map(int, second_elf_range.split('-'))
    return (first_elf_start <= second_elf_start <= first_elf_stop) or \
           (second_elf_start <= first_elf_start <= second_elf_stop)


def part_one(inp: list) -> int:
    return [is_fully_contained(first_elf_range=first_elf, second_elf_range=second_elf)
            for assignment in inp
            for first_elf, second_elf in (assignment.split(','), )].count(True)


def part_two(inp: list) -> int:
    return [ranges_overlap(first_elf_range=first_elf, second_elf_range=second_elf)
            for assignment in inp
            for first_elf, second_elf in (assignment.split(','), )].count(True)


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    result_part_two = part_two(inp)
    print(f"Result for part one: {result_part_one}")
    print(f"Result for part two: {result_part_two}")


if __name__ == '__main__':
    main()
