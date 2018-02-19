import re
from collections import defaultdict
from time import time

test_rules = {
    'H': ['HO', 'OH'],
    'O': ['HH']
}

test_input_1 = 'HOH'
test_input_2 = 'HOHOHO'
test_input_3 = 'OO2O'

with open('data.txt') as file:
    input_data = file.read().splitlines()

    # create ruleset
    input_ruleset = defaultdict(list)
    for line in input_data[:-2]:
        a, b = re.match(r'([A-Za-z]+) => ([A-Za-z]+)', line).groups()
        input_ruleset[a].append(b)

    # get seed molecule
    input_molecule = input_data[-1]


def solve(ruleset, seed_molecule):
    generated_molecules = set()

    # for every rule in ruleset, e.g. ['H','O']
    # find all matches of that rule, e.g. 'H' in 'HOH' => [(0,1), (2,3)]
    # and apply all possible replacements of the rule to those matches, e.g. 'H' => ['HO', 'OH']
    for rule in ruleset:
        for match in re.finditer(rule, seed_molecule):
            for replacement in ruleset[rule]:
                generated_molecules.add(seed_molecule[:match.start()] + replacement + seed_molecule[match.end():])

    return len(generated_molecules)


def main():
    test_1 = solve(test_rules, test_input_1)
    print('test_1:', test_1)
    test_2 = solve(test_rules, test_input_2)
    print('test_2:', test_2)
    test_3 = solve(test_rules, test_input_3)
    print('test_3:', test_3)

    start = time()
    answer = solve(input_ruleset, input_molecule)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
