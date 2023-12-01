TEST = True

test_path = ''
input_path = ''

file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]


def part_one():
    result = ''
    return result


def part_two():
    result = ''
    return result


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
