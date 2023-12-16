import re
import time

TEST = False
day = 11
file_path = f'data/test-{day}.txt' if TEST else f'data/day-{day}.txt'

with open(file_path, 'r') as f:
    data = [x.strip() for x in f]
    empty_rows = [x for x in range(len(data)) if len(set([y for y in data[x]])) == 1]
    empty_cols = [x for x in range(len(data[0])) if len(set([y[x] for y in data])) == 1]
    galaxies = [(x, galaxy.start()) for x, row in enumerate(data) for galaxy in re.finditer('(#)', row)]


def expanding_parts_on_route(galaxy1, galaxy2):
    cols = [col for col in empty_cols if min((galaxy1[1], galaxy2[1])) <= col <= max((galaxy1[1], galaxy2[1]))]
    rows = [row for row in empty_rows if min((galaxy1[0], galaxy2[0])) <= row <= max((galaxy1[0], galaxy2[0]))]
    return len(cols) + len(rows)


def part_one(number_of_expansions=1):
    result = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            galaxy1, galaxy2 = galaxies[i], galaxies[j]
            distance = abs(galaxy1[0]-galaxy2[0]) + abs(galaxy1[1]-galaxy2[1])
            expanding = expanding_parts_on_route(galaxy1, galaxy2)
            result += distance + (number_of_expansions * expanding)
    return result


def part_two():
    result = part_one(1000000 - 1)
    return result


if __name__ == '__main__':
    start_time = time.time()
    print(f'The solution for part 1 is: {part_one()} ({time.time()-start_time:.2f}s)')
    start_time = time.time()
    print(f'The solution for part 2 is: {part_two()} ({time.time()-start_time:.2f}s)')
