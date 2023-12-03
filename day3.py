import re

TEST = False

test_path = 'data/test-3.txt'
input_path = 'data/day-3.txt'

file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = ''.join([x.strip() for x in f.readlines()])
    grid_size = int(len(data) ** 0.5)


def get_adjacent_cells(coordinates):
    if type(coordinates) is not tuple:
        coordinates = position_to_grid_coordinates(coordinates)
    x_coord, y_coord = coordinates
    result = []
    for x, y in [(x_coord+i, y_coord+j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
        if (0 <= x < grid_size) and (0 <= y < grid_size):
            result.append([x, y])
    return result


def position_to_grid_coordinates(x):
    return x % grid_size, x // grid_size


def grid_coordinates_to_position(coordinates):
    x_coord, y_coord = coordinates
    return x_coord + (y_coord * grid_size)


def adjacent_to_symbol(coordinates, number_string):
    for coordinate in coordinates:
        adjacant_char = data[grid_coordinates_to_position(coordinate)]
        if re.match('[^\d\.]', adjacant_char):
            return int(number_string)
    return 0


def extract_integer_at_position(position):
    if position < 0 or position >= len(data):
        return None
    start = position
    end = position

    if data[position].isdigit():
        while start >= 0 and data[start].isdigit():
            start -= 1
        while end < len(data) and data[end].isdigit():
            end += 1
        return int(data[start + 1:end])

    return None


def part_one():
    result = 0
    numbers = re.finditer('(\d+)', data)
    for number in numbers:
        number_coordinates = {position_to_grid_coordinates(x) for x in range(number.start(), number.end())}
        adjacent_coordinates = set(tuple(cell) for x in range(number.start(), number.end()) for cell in get_adjacent_cells(x))
        adjacent_coordinates = adjacent_coordinates - number_coordinates
        result += adjacent_to_symbol(adjacent_coordinates, data[number.start():number.end()])
    return result


def part_two():
    result = 0
    gears = re.finditer('(\*)', data)
    for gear in gears:
        adjacent_coordinates = set(tuple(cell) for cell in get_adjacent_cells(gear.start()))
        adjacent_numbers = {extract_integer_at_position(grid_coordinates_to_position(adjacent_coord)) for adjacent_coord in adjacent_coordinates}
        adjacent_numbers.discard(None)

        if len(adjacent_numbers) == 2:
            adjacent_numbers = list(adjacent_numbers)
            result += (adjacent_numbers[0] * adjacent_numbers[1])
    return result


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
