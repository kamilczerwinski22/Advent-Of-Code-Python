from InputReader import read_fixed_input

SHAPE_POINT_VALUES = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3,
}

SINGLE_ROUND_POINTS = {
    'LOSE': 0,
    'DRAW': 3,
    'WIN': 6
}

OPPONENT_SHAPES = ['A', 'B', 'C']
PLAYER_SHAPES = ['X', 'Y', 'Z']


def calculate_single_round_score_with_player_shape(opponent_shape: str, player_shape: str) -> int:
    player_shape_idx = PLAYER_SHAPES.index(player_shape)
    opponent_shape_idx = OPPONENT_SHAPES.index(opponent_shape)
    player_shape_value = SHAPE_POINT_VALUES.get(player_shape)

    if opponent_shape_idx == 0 and player_shape_idx == len(PLAYER_SHAPES) - 1:  # LOSE
        return player_shape_value
    elif player_shape_idx > opponent_shape_idx or player_shape_idx == 0 \
            and opponent_shape_idx == len(OPPONENT_SHAPES) - 1:  # WIN
        return SINGLE_ROUND_POINTS.get('WIN') + player_shape_value
    elif player_shape_idx == opponent_shape_idx:  # DRAW
        return SINGLE_ROUND_POINTS.get('DRAW') + player_shape_value
    else:  # LOSE
        return player_shape_value


def part_one(inp: list) -> int:
    return sum(calculate_single_round_score_with_player_shape(opponent_shape=opponent_pick, player_shape=player_pick)
               for opponent_pick, player_pick in (pair.split(' ') for pair in inp))


def calculate_single_round_score_with_game_result(opponent_shape: str, game_result: str) -> int:
    opponent_pick_idx = OPPONENT_SHAPES.index(opponent_shape)
    if game_result == 'Z':  # WIN
        return SHAPE_POINT_VALUES.get((PLAYER_SHAPES + PLAYER_SHAPES[:1])[opponent_pick_idx + 1]) \
               + SINGLE_ROUND_POINTS.get('WIN')
    elif game_result == 'Y':  # DRAW
        return SHAPE_POINT_VALUES.get(opponent_shape) \
               + SINGLE_ROUND_POINTS.get('DRAW')  # Opponent's shape is the same as player's
    else:  # LOSE
        return SHAPE_POINT_VALUES.get((PLAYER_SHAPES[-1:] + PLAYER_SHAPES)[opponent_pick_idx]) \
               + SINGLE_ROUND_POINTS.get('LOSE')


def part_two(inp: list) -> int:
    return sum(calculate_single_round_score_with_game_result(opponent_shape=opponent_pick, game_result=game_result)
               for opponent_pick, game_result in (pair.split(' ') for pair in inp))


def main() -> None:
    inp = read_fixed_input()
    result_part_one = part_one(inp)
    result_part_two = part_two(inp)
    print(f"Result for part one: {result_part_one}")
    print(f"Result for part two: {result_part_two}")


if __name__ == '__main__':
    main()
