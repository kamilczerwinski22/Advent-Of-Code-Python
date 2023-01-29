from InputReader import readFixedInput

# A or X - Rock (1 point) / second half: X - lose, Y - draw, Z - win
# B or Y - Paper (2 points)
# C or Z - Scissors (3 points)
# lose - 0 points; draw - 3 points; win - 6 points

game_combinations_part1 = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6
}

game_combinations_part2 = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7
}


def partOne() -> int:
    all_games = readFixedInput()
    points = 0
    for single_round in all_games:
        opponent, player = single_round.split(' ')
        points += play_single_round(player, opponent)
    return points


def partTwo() -> int:
    all_games = readFixedInput()
    points = 0
    for single_round in all_games:
        opponent, to_pick = single_round.split(' ')
        points += play_single_round_part2(to_pick, opponent)
    return points


def play_single_round(player_pick: str, opponent_pick: str) -> int:
    return game_combinations_part1.get((opponent_pick, player_pick), 0)


def play_single_round_part2(to_pick: str, opponent_pick: str) -> int:
    return game_combinations_part2.get((opponent_pick, to_pick), 0)


if __name__ == '__main__':
    # print(f"Part one result: {partOne()}")
    print(f"Part two result: {partTwo()}")
