TEST = False
day = 7
test_path = f'data/test-{day}.txt'
input_path = f'data/day-{day}.txt'
file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip().split() for x in f.readlines()]


def get_rank_score(card: str, jokers: bool = False) -> int:
    return 'J23456789TJQKA'.find(card) + 1 if jokers else '23456789TJQKA'.find(card) + 1


def determine_hand_type(hand: str, jokers: bool = False) -> tuple:
    high_card = [get_rank_score(x, jokers) for x in hand]
    number_of_jokers = hand.count('J')
    hand = {x: sum(y == x for y in hand) for x in hand}
    symbols, amount = list(hand.keys()), list(hand.values())
    hand_size = len(symbols)
    if hand_size == 1:
        return 6, high_card
    elif hand_size == 2:
        if 4 in amount:
            if jokers and number_of_jokers in [1, 4]:
                return 6, high_card
            else:
                return 5, high_card
        elif 3 in amount and 2 in amount:
            if jokers and number_of_jokers == 2:
                return 6, high_card
            elif jokers and number_of_jokers == 3:
                return 6, high_card
            else:
                return 4, high_card
    elif hand_size == 3:
        if 3 in amount:
            if jokers and number_of_jokers in [1, 3]:
                return 5, high_card
            else:
                return 3, high_card
        else:
            if jokers and number_of_jokers == 1:
                return 4, high_card
            elif jokers and number_of_jokers == 2:
                return 5, high_card
            else:
                return 2, high_card
    elif hand_size == 4:
        if jokers and number_of_jokers in [1, 2]:
            return 3, high_card
        else:
            return 1, high_card
    elif hand_size == 5:
        if jokers and number_of_jokers == 1:
            return 1, high_card
        else:
            return 0, high_card


def part_one(jokers: bool = False) -> int:
    result = []
    for h in data:
        hand, bid = h
        score = determine_hand_type(hand, jokers)
        result.append([score[0], score[1], int(bid)])
    hand_ranks = sorted(result, key=lambda x: (x[0], x[1]), reverse=True)
    scores = [hand_ranks[x][2] * (len(hand_ranks)-x) for x in range(len(hand_ranks))]
    return sum(scores)


def part_two() -> int:
    return part_one(jokers=True)


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
