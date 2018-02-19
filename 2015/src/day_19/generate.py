import random
import re
from collections import defaultdict

with open('data.txt') as file:
    input_data = file.read().splitlines()
    input_ruleset = defaultdict(list)
    for line in input_data[:-2]:
        a, b = re.match(r'([A-Za-z]+) => ([A-Za-z]+)', line).groups()
        input_ruleset[a].append(b)


# function to generate molecules of arbitrary replacement step count according to the rules
def generate_random(ruleset, substitutions):
    generated_molecules = {'e'}

    for i in range(substitutions):
        new_molecules = set()

        molecule = random.choice(list(generated_molecules))
        for rule in ruleset:
            for match in re.finditer(rule, molecule):
                for replacement in ruleset[rule]:
                    new_molecules.add(molecule[:match.start()] + replacement + molecule[match.end():])

        generated_molecules = new_molecules

    print(str(substitutions) + ': ' + str(generated_molecules.pop()))


def main():
    generate_random(input_ruleset, 20)
    generate_random(input_ruleset, 21)
    generate_random(input_ruleset, 22)
    generate_random(input_ruleset, 23)


if __name__ == '__main__':
    main()
