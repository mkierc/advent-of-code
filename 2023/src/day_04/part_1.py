import re
from pprint import pprint

test_list = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]

card_list = []

with open("data.txt") as file:
    for _line in file.readlines():
        card_list.append(_line)


def parse_card(card):
    numbers = re.match(r'Card[ ]+\d+: ([\d ]+) \| ([\d ]+)', card).groups()
    winning_numbers = set(re.findall(r'\d+', numbers[0]))
    my_numbers = set(re.findall(r'\d+', numbers[1]))
    my_winning = winning_numbers.intersection(my_numbers)
    return int(2 ** (int(len(my_winning))-1))


def count_points(cards):
    points = 0

    for card in cards:
        points += parse_card(card)

    return points


def main():
    test = count_points(test_list)
    print("test:", test)

    answer = count_points(card_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# 888 too low