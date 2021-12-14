import collections
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
    pair_counts = collections.defaultdict(lambda: 0)
    element_counts = collections.defaultdict(lambda: 0)
    for x, y in list(zip(_polymer, _polymer[1:])):
        pair_counts[f'{x}{y}'] = pair_counts[f'{x}{y}'] + 1

    for i in range(steps):
        element_counts = collections.defaultdict(lambda: 0)
        new_pair_counts = collections.defaultdict(lambda: 0)
        for pair, count in pair_counts.items():
            x, y = pair
            z = _rules[pair]
            new_pair_counts[f'{x}{z}'] = new_pair_counts[f'{x}{z}'] + count
            new_pair_counts[f'{z}{y}'] = new_pair_counts[f'{z}{y}'] + count
            element_counts[f'{x}'] = element_counts[f'{x}'] + count
            element_counts[f'{z}'] = element_counts[f'{z}'] + count
        pair_counts = new_pair_counts

    # add last element of last pair
    element_counts[_polymer[-1]] = element_counts[_polymer[-1]] + 1

    counter = sorted(element_counts.values())
    return counter[-1] - counter[0]


def main():
    test = count_elements(test_starting_polymer, test_insertion_rules, 40)
    print("my test:", test)

    answer = count_elements(starting_polymer, insertion_rules, 40)
    print("answer:", answer)


if __name__ == "__main__":
    main()
