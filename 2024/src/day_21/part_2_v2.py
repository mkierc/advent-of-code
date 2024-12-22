import heapq
import re
from collections import defaultdict, Counter
from itertools import product, pairwise
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

    # arrows_to_arrows = {}
    #
    # for _from, _to in arrow_combinations:
    #     path_list = find_all_paths(_from, _to, arrow_positions)
    #     arrows_to_arrows.update({(_from, _to): path_list})

    arrows_to_arrows = {('<', '<'): [''],
                        ('<', '>'): ['>>'],
                        ('<', 'A'): ['>>^', '>^>'],  # '>>^' = 136_422, '>^>' = 138_798
                        ('<', '^'): ['>^'],
                        ('<', 'v'): ['>'],
                        ('>', '<'): ['<<'],
                        ('>', '>'): [''],
                        ('>', 'A'): ['^'],
                        ('>', '^'): ['<^', '^<'],  # eq 136_422
                        ('>', 'v'): ['<'],
                        ('A', '<'): ['v<<', '<v<'],  # 'v<<' = 132_376, '<v<' = 136_422
                        ('A', '>'): ['v'],
                        ('A', 'A'): [''],
                        ('A', '^'): ['<'],
                        ('A', 'v'): ['<v', 'v<'],  # eq 132_376
                        ('^', '<'): ['v<'],
                        ('^', '>'): ['v>', '>v'],  # eq 132_376
                        ('^', 'A'): ['>'],
                        ('^', '^'): [''],
                        ('^', 'v'): ['v'],
                        ('v', '<'): ['<'],
                        ('v', '>'): ['>'],
                        ('v', 'A'): ['>^', '^>'],  # eq 132_376
                        ('v', '^'): ['^'],
                        ('v', 'v'): ['']}
    pprint(arrows_to_arrows)

    keypad_to_arrows = defaultdict(list)

    for _from, _to in button_combinations:
        _from = '0'
        _to = '2'
        path_list = find_all_paths(_from, _to, keypad_positions)

        min_path = 1_000
        for path in path_list:
            decoded = decode(path, arrows_to_arrows)
            for i in range(25):
                print(i, len(decoded))
                decoded = decode(decoded, arrows_to_arrows)
            # print(decode(path, arrows_to_arrows), len(decode(path, arrows_to_arrows)))
            if len(decoded) < min_path:
                min_path = len(decoded)

        for path in path_list:
            double_decoded = decode(decode(path, arrows_to_arrows), arrows_to_arrows)
            if len(double_decoded) == min_path:
                keypad_to_arrows.update({(_from, _to): [*keypad_to_arrows[(_from, _to)], path]})

    pprint(keypad_to_arrows)
    pprint(arrows_to_arrows)

    return keypad_to_arrows, arrows_to_arrows


def build_short_mappings():
    keypad_arrows = {'00': 'A',
                     '01': '^<A',
                     '02': '^A',
                     '03': '^>A',
                     '04': '^^<A',
                     '05': '^^A',
                     '06': '^^>A',
                     '07': '^^^<A',
                     '08': '^^^A',
                     '09': '^^^>A',
                     '0A': '>A',
                     '10': '>vA',
                     '11': 'A',
                     '12': '>A',
                     '13': '>>A',
                     '14': '^A',
                     '15': '^>A',
                     '16': '^>>A',
                     '17': '^^A',
                     '18': '^^>A',
                     '19': '^^>>A',
                     '1A': '>>vA',
                     '20': 'vA',
                     '21': '<A',
                     '22': 'A',
                     '23': '>A',
                     '24': '<^A',
                     '25': '^A',
                     '26': '^>A',
                     '27': '<^^A',
                     '28': '^^A',
                     '29': '^^>A',
                     '2A': 'v>A',
                     '30': '<vA',
                     '31': '<<A',
                     '32': '<A',
                     '33': 'A',
                     '34': '<<^A',
                     '35': '<^A',
                     '36': '^A',
                     '37': '<<^^A',
                     '38': '<^^A',
                     '39': '^^A',
                     '3A': 'vA',
                     '40': '>vvA',
                     '41': 'vA',
                     '42': 'v>A',
                     '43': 'v>>A',
                     '44': 'A',
                     '45': '>A',
                     '46': '>>A',
                     '47': '^A',
                     '48': '^>A',
                     '49': '^>>A',
                     '4A': '>>vvA',
                     '50': 'vvA',
                     '51': '<vA',
                     '52': 'vA',
                     '53': 'v>A',
                     '54': '<A',
                     '55': 'A',
                     '56': '>A',
                     '57': '<^A',
                     '58': '^A',
                     '59': '^>A',
                     '5A': 'vv>A',
                     '60': '<vvA',
                     '61': '<<vA',
                     '62': '<vA',
                     '63': 'vA',
                     '64': '<<A',
                     '65': '<A',
                     '66': 'A',
                     '67': '<<^A',
                     '68': '<^A',
                     '69': '^A',
                     '6A': 'vvA',
                     '70': '>vvvA',
                     '71': 'vvA',
                     '72': 'vv>A',
                     '73': 'vv>>A',
                     '74': 'vA',
                     '75': 'v>A',
                     '76': 'v>>A',
                     '77': 'A',
                     '78': '>A',
                     '79': '>>A',
                     '7A': '>>vvvA',
                     '80': 'vvvA',
                     '81': '<vvA',
                     '82': 'vvA',
                     '83': 'vv>A',
                     '84': '<vA',
                     '85': 'vA',
                     '86': 'v>A',
                     '87': '<A',
                     '88': 'A',
                     '89': '>A',
                     '8A': 'vvv>A',
                     '90': '<vvvA',
                     '91': '<<vvA',
                     '92': '<vvA',
                     '93': 'vvA',
                     '94': '<<vA',
                     '95': '<vA',
                     '96': 'vA',
                     '97': '<<A',
                     '98': '<A',
                     '99': 'A',
                     '9A': 'vvvA',
                     'A0': '<A',
                     'A1': '^<<A',
                     'A2': '<^A',
                     'A3': '^A',
                     'A4': '^^<<A',
                     'A5': '<^^A',
                     'A6': '^^A',
                     'A7': '^^^<<A',
                     'A8': '<^^^A',
                     'A9': '^^^A',
                     'AA': 'A'
                     }

    # 264575170278504 too high
    # 105695191413198 too low

    arrows_arrows = {'<<': '',
                        '<>': '>>',
                        '<A': '>>^',#  '>>^' = 136_422, '>^>' = 138_798
                        '<^': '>^',
                        '<v': '>',
                        '><': '<<',
                        '>>': '',
                        '>A': '^',
                        '>^': '<^', #'^<',  # eq 136_422
                        '>v': '<',
                        'A<': 'v<<', #'<v<'  # 'v<<' = 132_376, '<v<' = 136_422
                        'A>': 'v',
                        'AA': '',
                        'A^': '<',
                        'Av': '<v', #'v<',  # eq 132_376
                        '^<': 'v<',
                        '^>': 'v>', #'>v',  # eq 132_376
                        '^A': '>',
                        '^^': '',
                        '^v': 'v',
                        'v<': '<',
                        'v>': '>',
                        'vA': '^>',  #'>^', # NOT EQ '^>' 232389969568832, '>^' 264575170278504
                        'v^': '^',
                        'vv': ''}
    # arrows_arrows = {'<<': '',
    #                  '<>': '>>',
    #                  '<A': '>>^',
    #                  '<^': '>^',
    #                  '<v': '>',
    #                  '><': '<<',
    #                  '>>': '',
    #                  '>A': '^',
    #                  '>^': '<^',
    #                  '>v': '<',
    #                  'A<': 'v<<',
    #                  'A>': 'v',
    #                  'AA': '',
    #                  'A^': '<',
    #                  'Av': '<v',
    #                  '^<': 'v<',
    #                  '^>': 'v>',
    #                  '^A': '>',
    #                  '^^': '',
    #                  '^v': 'v',
    #                  'v<': '<',
    #                  'v>': '>',
    #                  'vA': '>^',
    #                  'v^': '^',
    #                  'vv': '',
    #                  }
    #
    # # example:
    # #                         0               2                           9                         A
    # #             <           A         ^     A       >           ^ ^     A           v v v         A
    # #   v  < <    A  > >   ^  A    <    A  >  A   v   A    <   ^  A A  >  A    <  v   A A A  >   ^  A
    # # <vA <A A >>^A vA A <^A >A <v<A >>^A vA ^A <vA >^A <v<A >^A >A A vA ^A <v<A >A >^A A A vA <^A >A
    # keypad_short = {}
    #
    # for k, v in keypad_arrows.items():
    #     v = v[0]
    # vmap = defaultdict(int)
    # for i in range(len(v) - 1):
    #     vmap.update({(v[i], v[i + 1]): vmap[v[i], v[i + 1]] + 1})
    # print(k, vmap)
    # keypad_short.update({k, vmap})
    #
    # arrows_short = {}
    #
    # for k, v in arrows_arrows.items():
    #     v = v[0]
    # vmap = defaultdict(int)
    # for i in range(len(v) - 1):
    #     vmap.update({(v[i], v[i + 1]): vmap[v[i], v[i + 1]] + 1})
    # arrows_short.update({k, vmap})
    #
    # print(keypad_short)
    # print(arrows_short)

    return keypad_arrows, arrows_arrows


def short_decode(code_map, short_mapping):
    """Decode map of pair counts into decoded strings, and back into maps of pair counts:

    {'<A': 1, 'A^': 3, '^A': 1, ... }  ->  'A>>^A' x 1, 'AA' x 3, ...  ->  {'A>': 2, '>>': 1, ... }
    """

    decoded = defaultdict(int)

    for k, v in code_map.items():
        mapped = short_mapping[k]  # '<A' -> '>>^'
        paired = pairwise('A' + mapped + 'A')  # '>>^' -> 'A>>^A' -> ['A>', '>>', '>^', '^A']
        for a, b in paired:
            decoded.update({a + b: decoded[a + b] + v})

    return decoded


def decode(code, mapping):
    decoded = ''
    code = 'A' + code
    for a, b in pairwise(code):
        decoded += mapping[a + b]
    return dict(Counter([a + b for a, b in pairwise('A' + decoded)]))


def solve(code_list):
    keypad_short, arrows_short = build_short_mappings()

    complexity_sum = 0

    for code in code_list:
        # print(code)
        decoded = decode(code, keypad_short)
        # print(decoded)

        for i in range(25):
            print(i)
            decoded = short_decode(decoded, arrows_short)
            # print(decoded)

        complexity = sum([v for v in decoded.values()])
        numeric_code = int(re.findall(r'(\d+)', code)[0])
        # print(complexity, numeric_code, complexity * numeric_code)
        complexity_sum += complexity * numeric_code

    return complexity_sum


def main():
    # keypad_short, arrows_short = build_short_mappings()
    # pprint(keypad_short)
    # pprint(arrows_short)
    #
    # decoded = decode('029A', keypad_short)
    # print('decoded', decoded)

    # sh_decoded = short_decode({'<A': 1}, arrows_short)
    # print('short decoded', sh_decoded)

    test_1 = solve(test_codes)
    print('test_1:', test_1)

    start = time()
    answer = solve(codes)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()

# 264575170278504 too high
# 105695191413198 too low
