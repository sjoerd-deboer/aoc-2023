TEST = False
day = 9
file_path = f'data/test-{day}.txt' if TEST else f'data/day-{day}.txt'

with open(file_path, 'r') as f:
    data = [[int(y) for y in x.strip().split()] for x in f.readlines()]


def get_sequence(history):
    h, current_sequence = [history], history
    while any(current_sequence):
        current_sequence = [x[1]-x[0] for x in zip(current_sequence[:-1], current_sequence[1:])]
        h.append(current_sequence)
    return h


def part_one():
    result = []
    for history in data:
        sequence = get_sequence(history)
        new_value = sum([x[-1] for x in sequence])
        result.append(new_value)
    return sum(result)


def part_two():
    result = []
    for history in data:
        sequence = get_sequence(history)
        x = sequence[0][0]
        for r in range(1, len(sequence)):
            x += ((-1) ** r) * sequence[r][0]
        result.append(x)
    return sum(result)


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
