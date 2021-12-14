import collections
import copy
import re

test_starting_polymer = 'NNCB'

test_insertion_rules = {
    'CH': 'B',
    'HH': 'N',
    'CB': 'H',
    'NH': 'C',
    'HB': 'C',
    'HC': 'B',
    'HN': 'C',
    'NN': 'C',
    'BH': 'H',
    'NC': 'B',
    'NB': 'B',
    'BN': 'B',
    'BB': 'N',
    'BC': 'B',
    'CC': 'N',
    'CN': 'C',
}

rule_regex = re.compile(r'([A-Z]{2}) -> ([A-Z])')

insertion_rules = {}

with open("data.txt") as file:
    input_data = file.read().split('\n\n')
    starting_polymer = input_data[0]
    for rule in input_data[1].split('\n'):
        aa, b = re.findall(rule_regex, rule)[0]
        insertion_rules.update({aa: b})


def count_elements(_polymer, _rules, steps):
    polymer = copy.deepcopy(_polymer)
    for i in range(steps):
        new_polymer = polymer[0]
        for x, y in list(zip(polymer, polymer[1:])):
            z = _rules.get(f'{x}{y}')
            new_polymer += f'{z}{y}'
        polymer = new_polymer
    counter = collections.Counter(list(zip(polymer))).most_common()
    return counter[0][1] - counter[-1][1]


def main():
    test = count_elements(test_starting_polymer, test_insertion_rules, 10)
    print("test:", test)

    answer = count_elements(starting_polymer, insertion_rules, 10)
    print("answer:", answer)


if __name__ == "__main__":
    main()
