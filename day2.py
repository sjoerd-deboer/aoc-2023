TEST = False

test_path = 'data/test-2.txt'
input_path = 'data/day-2.txt'

file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]


def game_possible(red, green, blue, game):
    game_id, subsets_str = game.split(':')
    game_id = int(game_id.split()[1])
    subsets = [x.strip() for x in subsets_str.strip().split(';')]

    for subset in subsets:
        cubes = {color: 0 for color in ['red', 'green', 'blue']}
        for color_info in subset.split(', '):
            amount, color = color_info.split()
            cubes[color] += int(amount)
        if cubes['red'] > red or cubes['green'] > green or cubes['blue'] > blue:
            return 0
    return game_id


def power_of_a_game(game):
    subsets = [x.strip() for x in game.split(':')[1].strip().split(';')]
    cubes = {color: 0 for color in ['red', 'green', 'blue']}
    for subset in subsets:
        for color_info in subset.split(', '):
            amount, color = color_info.split()
            if int(amount) > cubes[color]:
                cubes[color] = int(amount)
    return cubes['red'] * cubes['green'] * cubes['blue']


def part_one(red, green, blue):
    result = [game_possible(red, green, blue, game) for game in data]
    return sum(result)


def part_two():
    result = [power_of_a_game(game) for game in data]
    return sum(result)


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one(12, 13, 14)} ')
    print(f'The solution for part 2 is: {part_two()}')
