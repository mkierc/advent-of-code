import heapq
import itertools
import re
from collections import defaultdict
from functools import cmp_to_key
from itertools import product
from pprint import pprint
from time import time

test_input = '''029A
980A
179A
456A
379A'''

test_codes = test_input.split()

with open('data.txt') as file:
    codes = file.read().split()

robot_map_1 = {}


def comparator():
    # ordering: go left at the end, and then press accept
    ordering = '<', '>', '^', 'v', 'A'

    def cmp(a, b):
        if ordering.index(a) > ordering.index(b):
            return 1
        elif ordering.index(a) == ordering.index(b):
            return 0
        else:
            return -1

    return cmp


def find_path(_from, _to, keypad_map):
    # v ^ < >
    # directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # v < ^ >
    # directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    # < v ^ >
    # directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    # v ^ > <
    # directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    # > v ^ <
    # directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    # > < v ^
    # directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    # < v > ^
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    start = keypad_map[_from]
    end = keypad_map[_to]

    queue = []
    heapq.heappush(queue, (0, start, directions[0]))

    visited_nodes = defaultdict(tuple)
    cost_to_node = defaultdict(lambda: 1_000_000_000)

    visited_nodes[start] = ()
    cost_to_node[start] = 0

    while queue:
        (x, y), (dx, dy) = heapq.heappop(queue)[1:]

        new_moves = []
        for d_x, d_y in directions:
            if (x + d_x, y + d_y) in keypad_map.values():
                new_moves.append((x + d_x, y + d_y, d_x, d_y))

        for n_x, n_y, d_x, d_y in new_moves:
            new_cost = cost_to_node[(x, y)] + 1

            if (n_x, n_y) not in cost_to_node or new_cost < cost_to_node[(n_x, n_y)]:
                cost_to_node[(n_x, n_y)] = new_cost
                directionality = 0 if dx == d_x and dy == d_y else 1
                priority = new_cost + directionality
                heapq.heappush(queue, (priority, (n_x, n_y), (d_x, d_y)))
                visited_nodes[(n_x, n_y)] = (x, y)

        # retrace, and save directions as keystrokes
        if (x, y) == end:
            moves = []
            current = x, y

            while visited_nodes[current]:
                px, py = visited_nodes[current]

                if px + 1 == x:
                    moves.insert(0, '>')
                elif px - 1 == x:
                    moves.insert(0, '<')
                elif py + 1 == y:
                    moves.insert(0, '^')
                elif py - 1 == y:
                    moves.insert(0, 'v')

                x, y = px, py
                current = x, y

            return ''.join(sorted(moves, key=cmp_to_key(comparator())))


def build_robot_mappings():
    buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
    arrows = ['<', '>', '^', 'v', 'A']

    button_combinations = [x for x in product(buttons, buttons)]
    arrow_combinations = [x for x in product(arrows, arrows)]

    keypad_positions = {
        '7': (0, 3), '8': (1, 3), '9': (2, 3),
        '4': (0, 2), '5': (1, 2), '6': (2, 2),
        '1': (0, 1), '2': (1, 1), '3': (2, 1),
        '0': (1, 0), 'A': (2, 0),
    }

    arrow_positions = {
        '^': (1, 1), 'A': (2, 1),
        '<': (0, 0), 'v': (1, 0), '>': (2, 0),
    }

    keypad_to_arrows = {}

    for _from, _to in button_combinations:
        path = find_path(_from, _to, keypad_positions)
        keypad_to_arrows.update({(_from, _to): path})

    arrows_to_arrows = {}

    for _from, _to in arrow_combinations:
        path = find_path(_from, _to, arrow_positions)
        arrows_to_arrows.update({(_from, _to): path})

    pprint(keypad_to_arrows)
    pprint(arrows_to_arrows)
    return keypad_to_arrows, arrows_to_arrows


def decode(code, mapping):
    decoded = ''
    decoded += mapping[('A', code[0])]
    decoded += 'A'
    for i in range(len(code) - 1):
        decoded += mapping[(code[i], code[i + 1])]
        decoded += 'A'

    return decoded


def solve(code_list):
    keypad_to_arrows = {('0', '0'): '',
                        ('0', '1'): '<^',
                        ('0', '2'): '^',
                        ('0', '3'): '>^',
                        ('0', '4'): '<^^',
                        ('0', '5'): '^^',
                        ('0', '6'): '>^^',
                        ('0', '7'): '<^^^',
                        ('0', '8'): '^^^',
                        ('0', '9'): '>^^^',
                        ('0', 'A'): '>',
                        ('1', '0'): '>v',
                        ('1', '1'): '',
                        ('1', '2'): '>',
                        ('1', '3'): '>>',
                        ('1', '4'): '^',
                        ('1', '5'): '>^',
                        ('1', '6'): '>>^',
                        ('1', '7'): '^^',
                        ('1', '8'): '>^^',
                        ('1', '9'): '>>^^',
                        ('1', 'A'): '>>v',
                        ('2', '0'): 'v',
                        ('2', '1'): '<',
                        ('2', '2'): '',
                        ('2', '3'): '>',
                        ('2', '4'): '<^',
                        ('2', '5'): '^',
                        ('2', '6'): '>^',
                        ('2', '7'): '<^^',
                        ('2', '8'): '^^',
                        ('2', '9'): '>^^',
                        ('2', 'A'): '>v',
                        ('3', '0'): '<v',
                        ('3', '1'): '<<',
                        ('3', '2'): '<',
                        ('3', '3'): '',
                        ('3', '4'): '<<^',
                        ('3', '5'): '<^',
                        ('3', '6'): '^',
                        ('3', '7'): '<<^^',
                        ('3', '8'): '<^^',
                        ('3', '9'): '^^',
                        ('3', 'A'): 'v',
                        ('4', '0'): '>vv',
                        ('4', '1'): 'v',
                        ('4', '2'): '>v',
                        ('4', '3'): '>>v',
                        ('4', '4'): '',
                        ('4', '5'): '>',
                        ('4', '6'): '>>',
                        ('4', '7'): '^',
                        ('4', '8'): '>^',
                        ('4', '9'): '>>^',
                        ('4', 'A'): '>>vv',
                        ('5', '0'): 'vv',
                        ('5', '1'): '<v',
                        ('5', '2'): 'v',
                        ('5', '3'): '>v',
                        ('5', '4'): '<',
                        ('5', '5'): '',
                        ('5', '6'): '>',
                        ('5', '7'): '<^',
                        ('5', '8'): '^',
                        ('5', '9'): '>^',
                        ('5', 'A'): '>vv',
                        ('6', '0'): '<vv',
                        ('6', '1'): '<<v',
                        ('6', '2'): '<v',
                        ('6', '3'): 'v',
                        ('6', '4'): '<<',
                        ('6', '5'): '<',
                        ('6', '6'): '',
                        ('6', '7'): '<<^',
                        ('6', '8'): '<^',
                        ('6', '9'): '^',
                        ('6', 'A'): 'vv',
                        ('7', '0'): '>vvv',
                        ('7', '1'): 'vv',
                        ('7', '2'): '>vv',
                        ('7', '3'): '>>vv',
                        ('7', '4'): 'v',
                        ('7', '5'): '>v',
                        ('7', '6'): '>>v',
                        ('7', '7'): '',
                        ('7', '8'): '>',
                        ('7', '9'): '>>',
                        ('7', 'A'): '>>vvv',
                        ('8', '0'): 'vvv',
                        ('8', '1'): '<vv',
                        ('8', '2'): 'vv',
                        ('8', '3'): '>vv',
                        ('8', '4'): '<v',
                        ('8', '5'): 'v',
                        ('8', '6'): '>v',
                        ('8', '7'): '<',
                        ('8', '8'): '',
                        ('8', '9'): '>',
                        ('8', 'A'): '>vvv',
                        ('9', '0'): '<vvv',
                        ('9', '1'): '<<vv',
                        ('9', '2'): '<vv',
                        ('9', '3'): 'vv',
                        ('9', '4'): '<<v',
                        ('9', '5'): '<v',
                        ('9', '6'): 'v',
                        ('9', '7'): '<<',
                        ('9', '8'): '<',
                        ('9', '9'): '',
                        ('9', 'A'): 'vvv',
                        ('A', '0'): '<',
                        ('A', '1'): '^<<',
                        ('A', '2'): '<^',
                        ('A', '3'): '^',
                        ('A', '4'): '^^<<',
                        ('A', '5'): '<^^',
                        ('A', '6'): '^^',
                        ('A', '7'): '^^^<<',
                        ('A', '8'): '<^^^',
                        ('A', '9'): '^^^',
                        ('A', 'A'): ''}
    arrows_to_arrows = {('<', '<'): '',
                        ('<', '>'): '>>',
                        ('<', 'A'): '>>^',
                        ('<', '^'): '>^',
                        ('<', 'v'): '>',
                        ('>', '<'): '<<',
                        ('>', '>'): '',
                        ('>', 'A'): '^',
                        ('>', '^'): '<^',
                        ('>', 'v'): '<',
                        ('A', '<'): '<v<',
                        ('A', '>'): 'v',
                        ('A', 'A'): '',
                        ('A', '^'): '<',
                        ('A', 'v'): '<v',
                        ('^', '<'): '<v',
                        ('^', '>'): '>v',
                        ('^', 'A'): '>',
                        ('^', '^'): '',
                        ('^', 'v'): 'v',
                        ('v', '<'): '<',
                        ('v', '>'): '>',
                        ('v', 'A'): '>^',
                        ('v', '^'): '^',
                        ('v', 'v'): ''}

    complexity_sum = 0

    for code in code_list:
        print(code)
        decoded = decode(code, keypad_to_arrows)
        print(decoded)
        decoded = decode(decoded, arrows_to_arrows)
        print(decoded)
        decoded = decode(decoded, arrows_to_arrows)
        print(decoded)
        complexity = len(decoded)
        numeric_code = int(re.findall(r'(\d+)', code)[0])
        print(complexity, numeric_code, complexity * numeric_code)
        complexity_sum += complexity * numeric_code

    return complexity_sum


def main():
    # todo: this solution doesn't work, but should be salvagable - need to find a way to use the mapping generator,
    #  instead of hardcoding hand-picked magic values...
    test_1 = solve(test_codes)
    print('test_1:', test_1)

    # start = time()
    # answer = solve(codes)
    # print('time:', time() - start)
    # print('answer:', answer)


if __name__ == '__main__':
    main()


# 190416 too high


# example:
# <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
#   v  < <    A  > >   ^  A    <    A  >  A   v   A    <   ^  A A  >  A    <  v   A A A  >   ^  A
#             <           A         ^     A       >           ^ ^     A           v v v         A
#                         0               2                           9                         A

# mine
# <v<A >A <A >^>A vA <^A v>A ^A <v<A >^>A vA ^A <v<A >^>A A <vA >A ^A <A >A <v<A >A ^>A A A <A v>A ^A
#    <  v  <    A  >   ^   >  A    <    A  >  A    <    A A   v  >  A  ^  A    <  v   A A A  ^   >  A
#               <             A         ^     A         ^ ^         >     A           v v v         A
#                             0               2                           9                         A

# mine (68):
#               3                                        7               9                         A
#         ^     A            ^ ^           < <           A       > >     A           v v v         A
#    <    A  >  A       <    A A   v  <    A A  > >   ^  A   v   A A  ^  A   v  <    A A A  >   ^  A
# v<<A >>^A vA ^A    v<<A >>^A A v<A <A >>^A A vA A ^<A >A v<A >^A A <A >A v<A <A >>^A A A vA ^<A >A


# best (64):
#               3                                        7               9                             A
#         ^     A                < <         ^ ^         A       > >     A               v v v         A
#    <    A  >  A      v  < <    A A  >   ^  A A  >      A   v   A A  ^  A    <  v       A A A  >   ^  A

# <v<A >>^A vA ^A    <vA <A A >>^A A vA <^A >A A vA     ^A <vA >^A A <A >A <v<A >A     >^A A A vA <^A >A

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


# v<A<AA>>^AvA<^A>Av<A<A>>^AvAA<^A>Av<<A>>^AAvA^Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A   min
# <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A


# real answers
# 029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# 980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
# 179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# 456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
# 379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

# mine:
# 029A: <vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A
# 980A: v<<A>>^AAAvA^A<vA<AA>>^AvAA<^A>Av<<A>A>^AAAvA<^A>A<vA>^A<A>A
# 179A: v<<A>>^Av<<A>A>^AAvAA<^A>Av<<A>>^AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A
# 456A: v<<A>>^AAv<<A>A>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>Av<<A>A>^AAvA<^A>A
# 379A: v<<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A


#         v <<   A >>  ^ A   <   A>AvA<^AA>A<vAAA>^A
#       <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#       <vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A
