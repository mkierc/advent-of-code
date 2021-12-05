import copy
import re

bingo_regex = re.compile(r'(\d+)')


class BingoBoard(object):
    def __init__(self, board):
        self.board = [int(x) for x in re.findall(bingo_regex, board)]
        self.marked_fields = set()
        self.is_won = False
        self.score = 0
        for number in self.board:
            self.score += number

    def mark(self, number):
        if number in self.board:
            self.marked_fields.add(self.board.index(number))
            self.score -= number
            if self._check_winning_conditions():
                self.is_won = True

    def _check_winning_conditions(self):
        # horizontal
        if ({0, 1, 2, 3, 4}.issubset(self.marked_fields)
            or {5, 6, 7, 8, 9}.issubset(self.marked_fields)
            or {10, 11, 12, 13, 14}.issubset(self.marked_fields)
            or {15, 16, 17, 18, 19}.issubset(self.marked_fields)
            or {20, 21, 22, 23, 24}.issubset(self.marked_fields)
            # vertical
            or {0, 5, 10, 15, 20}.issubset(self.marked_fields)
            or {1, 6, 11, 16, 21}.issubset(self.marked_fields)
            or {2, 7, 12, 17, 22}.issubset(self.marked_fields)
            or {3, 8, 13, 18, 23}.issubset(self.marked_fields)
            or {4, 9, 14, 19, 24}.issubset(self.marked_fields)
        ):
            return True
        return False

    def __repr__(self):
        return str(self.board)

    def __eq__(self, other):
        if not isinstance(other, BingoBoard):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (self.board == other.board and
                self.marked_fields == other.marked_fields and
                self.is_won == other.is_won and
                self.score == other.score)


test_drawn_numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

test_boards = [
    BingoBoard('''
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19
'''),
    BingoBoard('''
 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

'''),
    BingoBoard('''
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
''')
]

drawn_numbers = []
boards = []

with open("data.txt") as file:
    for number in file.readline().split(','):
        drawn_numbers.append(int(number))
    for line in file.read().split('\n\n'):
        boards.append(BingoBoard(line))


def find_last_winning_board(drawn_numbers, boards):
    for number in drawn_numbers:
        for board in boards:
            board.mark(number)
        for board in boards:
            if board.is_won:
                if len(boards) == 1:
                    return board.score * number
                new_boards = copy.deepcopy(boards)
                new_boards.remove(board)
                boards = new_boards


def main():
    test = find_last_winning_board(test_drawn_numbers, test_boards)
    print("test:", test)

    answer = find_last_winning_board(drawn_numbers, boards)
    print("answer:", answer)


if __name__ == "__main__":
    main()
