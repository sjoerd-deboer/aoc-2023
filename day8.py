from math import gcd

TEST = False
day = 8
file_path = f'data/test-{day}.txt' if TEST else f'data/day-{day}.txt'

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]
    instruction, data = data[0], data[2:]
    data = {key: next_element[1:-1].split(', ') for key, next_element in [x.split(' = ') for x in data]}


def lcm(l: list) -> int:
    l_c_m = 1
    for node in l:
        l_c_m = l_c_m * node // gcd(l_c_m, node)
    return l_c_m


def part_one(start_node: str, end_node: str) -> int:
    counter, current_node, current_instruction = 0, start_node, instruction[0]
    while True:
        if current_node[-len(end_node):] == end_node:
            break
        current_node = data[current_node][current_instruction == "R"]
        current_instruction = instruction[(counter + 1) % len(instruction)]
        counter += 1
    return counter


def part_two(end_node: str) -> int:
    return lcm([part_one(x, end_node) for x in [x for x in data.keys() if x[-1] == "A"]])


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one("AAA", "ZZZ")} ')
    print(f'The solution for part 2 is: {part_two("Z")} ')
