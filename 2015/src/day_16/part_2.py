import re

import time

aunt_regex = re.compile(r'Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)')

with open('data.txt') as file:
    input_data = file.read().splitlines()


class Aunt:
    def __init__(self, aunt_id, compounds):
        self.aunt_id = aunt_id
        self.compounds = {
            'children': -1,
            'cats': -1,
            'samoyeds': -1,
            'pomeranians': -1,
            'akitas': -1,
            'vizslas': -1,
            'goldfish': -1,
            'trees': -1,
            'cars': -1,
            'perfumes': -1
        }
        self.compounds.update(compounds)

    def __repr__(self):
        return str(self.aunt_id) + ' ' + str(self.compounds) + '\n'


def solve(raw_data):
    aunts = []

    for line in raw_data:
        aunt_id, compound_1, value_1, compound_2, value_2, compound_3, value_3 = re.match(aunt_regex, line).groups()
        new_aunt = Aunt(int(aunt_id), {compound_1: int(value_1), compound_2: int(value_2), compound_3: int(value_3)})
        aunts.append(new_aunt)

    for aunt in aunts:
        if (aunt.compounds['children'] == -1 or aunt.compounds['children'] == 3) \
                and (aunt.compounds['cats'] == -1 or aunt.compounds['cats'] > 7) \
                and (aunt.compounds['samoyeds'] == -1 or aunt.compounds['samoyeds'] == 2) \
                and (aunt.compounds['pomeranians'] == -1 or aunt.compounds['pomeranians'] < 3) \
                and (aunt.compounds['akitas'] == -1 or aunt.compounds['akitas'] == 0) \
                and (aunt.compounds['vizslas'] == -1 or aunt.compounds['vizslas'] == 0) \
                and (aunt.compounds['goldfish'] == -1 or aunt.compounds['goldfish'] < 5) \
                and (aunt.compounds['trees'] == -1 or aunt.compounds['trees'] > 3) \
                and (aunt.compounds['cars'] == -1 or aunt.compounds['cars'] == 2) \
                and (aunt.compounds['perfumes'] == -1 or aunt.compounds['perfumes'] == 1):
            return aunt


def main():
    start = time.time()
    answer = solve(input_data)
    print('time:', time.time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
