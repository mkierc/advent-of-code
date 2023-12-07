import functools

test_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

game = ''

with open("data.txt") as file:
    for _line in file.readlines():
        game += _line


@functools.total_ordering
class Hand:
    values = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    def __init__(self, _card_list, _bid):
        self.card_list = []
        for card in _card_list:
            self.card_list.append(self.values[card])

        self.bid = _bid
        self.hand_type = self._hand_type()

    def _hand_type(self):
        count = {}
        for card in self.card_list:
            if card in count:
                count[card] = count[card] + 1
            else:
                count[card] = 1

        ranks = sorted(count.values())

        if ranks == [5]:
            return 6
        if ranks == [1, 4]:
            return 5
        if ranks == [2, 3]:
            return 4
        if ranks == [1, 1, 3]:
            return 3
        if ranks == [1, 2, 2]:
            return 2
        if ranks == [1, 1, 1, 2]:
            return 1
        if ranks == [1, 1, 1, 1, 1]:
            return 0
        raise AssertionError("Unknown card set")

    def __eq__(self, other):
        return self.card_list == other.card_list

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        if self.hand_type > other.hand_type:
            return False
        if self.hand_type == other.hand_type:
            if self.card_list[0] < other.card_list[0]:
                return True
            if self.card_list[0] > other.card_list[0]:
                return False
            if self.card_list[1] < other.card_list[1]:
                return True
            if self.card_list[1] > other.card_list[1]:
                return False
            if self.card_list[2] < other.card_list[2]:
                return True
            if self.card_list[2] > other.card_list[2]:
                return False
            if self.card_list[3] < other.card_list[3]:
                return True
            if self.card_list[3] > other.card_list[3]:
                return False
            if self.card_list[4] < other.card_list[4]:
                return True
            if self.card_list[4] > other.card_list[4]:
                return False
            if self.card_list[5] < other.card_list[5]:
                return True
            if self.card_list[5] > other.card_list[5]:
                return False
        return False

    def __repr__(self):
        return str(self.card_list) + ' ' + str(self.bid) + ' ' + str(self.hand_type)


def rank_cards(_game):
    card_list = []

    for cards in _game.split('\n'):
        card, bid = cards.split(' ')
        card_list.append(Hand(card, int(bid)))

    winnings = 0
    for i, card in enumerate(sorted(card_list)):
        winnings += (i + 1) * card.bid

    return winnings


def main():
    test = rank_cards(test_input)
    print("test:", test)

    answer = rank_cards(game)
    print("answer:", answer)


if __name__ == "__main__":
    main()
