from itertools import combinations

TEST = True
day = 5
test_path = f'data/test-{day}.txt'
input_path = f'data/day-{day}.txt'
file_path = test_path if TEST else input_path


with open(file_path, 'r') as f:
    data = f.read().split('\n\n')
    seed, data = data[0], data[1:]
    seed = [int(x) for x in seed.split(' ')[1:]]
    maps = {}
    ranges = []
    for r in data:
        line = r.split('\n')
        meta, content = line[0], line[1:]
        meta = meta.split()[0].split('-to-')
        content = [[int(x) for x in line.split()] for line in content]
        print(content)
        for c in content:
            result = c[1] - c[0]
            c_r = (c[1], c[1]+c[2])
            ranges += [[c_r, result]]
        maps.update({meta[0]: {'ranges': content, 'next': meta[1], }})


def translate_number(number, ranges):
    for r in ranges:
        if r[1] <= number < r[1] + r[2]:
            return number + (r[0] - r[1])
    return number


def part_one(current, numbers):
    if current == 'location':
        return min(numbers)
    c = maps[current]
    n = c['next']
    translated_numbers = [translate_number(x, c['ranges']) for x in numbers]
    return part_one(n, translated_numbers)


def part_two(current):
    # find all combinations of intervals
    current_map = maps[current]
    current_map_ranges = current_map['ranges']
    next_map = maps[current_map['next']]
    print(f'Current: {current_map}')
    print(f'Next: {next_map}')


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one("seed", seed)} ')
    print(f'The solution for part 2 is: {part_two("seed")} ')
