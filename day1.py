TEST = False

test_path = 'data/test-1.txt'
input_path = 'data/day-1.txt'

file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]


def find_first_digit(l):
    l = list(l)
    for d in l:
        if d.isdigit():
            return d
    return False


def part_one():
    total = 0
    for line in data:
        first_digit = find_first_digit(line)
        last_digit = find_first_digit(line[::-1])
        total += int(first_digit + last_digit)
    return total


def part_two():
    string_to_int = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    total = 0
    for line in data:
        for s in string_to_int:
            line = line.replace(s, s + string_to_int[s] + s)
        first_digit = find_first_digit(line)
        last_digit = find_first_digit(line[::-1])
        total += int(first_digit + last_digit)
    return total


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
