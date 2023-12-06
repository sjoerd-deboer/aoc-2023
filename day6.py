TEST = False
day = 6
test_path = f'data/test-{day}.txt'
input_path = f'data/day-{day}.txt'
file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]
    time, distance = data
    time = [y.strip() for y in time.split()]
    distance = [y.strip() for y in distance.split()]
    time2 = int(''.join(time[1:]))
    distance2 = int(''.join(distance[1:]))
    data = [[int(a), int(b)] for a, b in zip(time[1:], distance[1:])]


def part_one():
    result = 1
    for race in data:
        winning = [y for y in [x * (race[0] - x) for x in range(1, race[0])] if y > race[1]]
        result = result * len(winning)
    return result


def part_two():
    result = 0
    for x in range(1, time2):
        result += int((x * (time2 - x)) > distance2)
    return result


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
