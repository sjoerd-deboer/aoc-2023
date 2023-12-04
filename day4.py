TEST = False

test_path = 'data/test-4.txt'
input_path = 'data/day-4.txt'

file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip() for x in f.readlines()]
    cards = dict()
    for card in data:
        card_meta, card_numbers = card.split(':')
        card_number = card_meta.split()[1]
        winning_numbers, card_numbers = card_numbers.split(' | ')
        winning_numbers = [int(x.strip()) for x in winning_numbers.split()]
        card_numbers = [int(x.strip()) for x in card_numbers.split()]
        winning_numbers = [x for x in card_numbers if x in winning_numbers]
        cards[int(card_number)] = winning_numbers


def part_one():
    result = 0
    for key, value in cards.items():
        result += (2 ** (len(value) - 1)) // 1
    return int(result)


def part_two():
    b = {c: 1 for c in cards.keys()}
    max_card = max(cards.keys())
    total = len(cards)
    while any(b.values()):
        b2 = {c: 0 for c in cards.keys()}
        for number, amount in b.items():
            b[number] = 0
            new_cards = [number + x for x in range(1, len(cards[number]) + 1) if number + x <= max_card]
            for new_card in new_cards:
                b2[new_card] = b2[new_card] + amount
            total += len(new_cards) * amount
        b = b2.copy()
    return total


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
