TEST = False
day = 7
test_path = f'data/test-{day}.txt'
input_path = f'data/day-{day}.txt'
file_path = test_path if TEST else input_path

with open(file_path, 'r') as f:
    data = [x.strip().split() for x in f.readlines()]

CARD_DECK = '23456789TJQKA'
TYPE_SCORE = len(CARD_DECK) + 1

def get_rank_score(card):
    return CARD_DECK.find(card) + 1


def part_one():
    result = []
    for h in data:
        hand, bid = h
        hand = {x: sum(y == x for y in hand) for x in hand}
        symbols, amount = list(hand.keys()), list(hand.values())
        hand = list(zip(symbols, amount))
        hand_size = len(hand)
        print(h[0], hand)
        score, score2, score3 = 0, 0, 0
        if hand_size == 1:
            print("Five of a kind")
            score = (6 * TYPE_SCORE) + get_rank_score(hand[0][0])
        elif hand_size == 2:
            if amount.count(4):
                print('Four of a kind')
                score = (5 * TYPE_SCORE) + get_rank_score(symbols[amount.index(4)])
                score2 = get_rank_score(symbols[amount.index(1)])
            else:
                print('Full house')
                average_rank = (get_rank_score(symbols[amount.index(3)]) + get_rank_score(symbols[amount.index(2)]))/2
                score = (4 * TYPE_SCORE) + average_rank
                score2 = get_rank_score(symbols[amount.index(2)])
        elif hand_size == 3:
            if amount.count(3):
                print('Three of a kind')
                score = (3 * TYPE_SCORE) + get_rank_score(symbols[amount.index(3)])
                # TODO: Fix this.
                score2 = get_rank_score(symbols[amount.index(1)])
            else:
                print('Two pair')
                average_rank = [get_rank_score(a) for a, b in hand if b == 2]
                score = (2 * TYPE_SCORE) + min(average_rank)/4 + max(average_rank)/2
        elif hand_size == 4:
            print('One pair')
            score = (1 * TYPE_SCORE) + get_rank_score(symbols[amount.index(2)])
        elif hand_size == 5:
            score = max([get_rank_score(x) for x in h[0]])
        result.append([h[0], score, bid])
    print(result)
    result.sort(key=lambda x: x[0])
    return sum([(x+1) * int(result[x][2]) for x in range(len(result))])


def part_two():
    result = data
    return result


if __name__ == '__main__':
    print(f'The solution for part 1 is: {part_one()} ')
    print(f'The solution for part 2 is: {part_two()} ')
