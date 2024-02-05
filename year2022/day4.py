from InputReader import read_fixed_input


def part_one(inp: list) -> int:
    for assignment in inp:
        first_elf, second_elf = assignment.split(',')
        first_elf_start, first_elf_stop = map(int, first_elf.split('-'))
        print(first_elf_start)


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    print(f"Result for part one: {result_part_one}")


if __name__ == '__main__':
    main()
