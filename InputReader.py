def read_fixed_input() -> list:
    with open("../input.txt") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]