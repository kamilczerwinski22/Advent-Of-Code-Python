from InputReader import readFixedInput
from itertools import groupby


def partOne() -> int:
    inp = readFixedInput()
    elfs = (sum(int(food) for food in elf) for element, elf in groupby(inp, key=lambda x: x != '') if element)
    return max(elfs)


def partTwo(top_snacks: int) -> int:
    inp = readFixedInput()
    elfs = list(sum(int(food) for food in elf) for element, elf in groupby(inp, key=lambda x: x != '') if element)
    top_snacks_list = []
    for _ in range(top_snacks):
        top_snacks_list.append(elfs.pop(elfs.index(max(elfs))))
    return sum(top_snacks_list)


if __name__ == '__main__':
    print(f"Part one result: {partOne()}")
    print(f"Part two result: {partTwo(top_snacks=3)}")
