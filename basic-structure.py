TEST = True
day = 0
file_path = f'data/test-{day}.txt' if TEST else f'data/day-{day}.txt'

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]


def part_one():
    result = data
    return result


def part_two():
    result = data
    return result


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
