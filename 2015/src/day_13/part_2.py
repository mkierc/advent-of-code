import itertools
import re

test_input_1 = [
    'Alice would gain 54 happiness units by sitting next to Bob.',
    'Alice would lose 79 happiness units by sitting next to Carol.',
    'Alice would lose 2 happiness units by sitting next to David.',
    'Bob would gain 83 happiness units by sitting next to Alice.',
    'Bob would lose 7 happiness units by sitting next to Carol.',
    'Bob would lose 63 happiness units by sitting next to David.',
    'Carol would lose 62 happiness units by sitting next to Alice.',
    'Carol would gain 60 happiness units by sitting next to Bob.',
    'Carol would gain 55 happiness units by sitting next to David.',
    'David would gain 46 happiness units by sitting next to Alice.',
    'David would lose 7 happiness units by sitting next to Bob.',
    'David would gain 41 happiness units by sitting next to Carol.'
]

# using regexes makes me really happy...
regex_of_happiness = re.compile(r'([A-Za-z]+) would (lose|gain) (\d+) happiness units by sitting next to ([A-Za-z]+).')

with open('data.txt') as file:
    input_data = file.read().splitlines()


def parse(raw_data):
    people = set()
    happiness_data = {}

    for line in raw_data:
        person_1, sign, value, person_2 = re.match(regex_of_happiness, line).groups()
        people.add(person_1)
        happiness_data.update({(person_1, person_2): int(value) if sign == 'gain' else -int(value)})

    # add myself to happiness data and people
    for person in people:
        happiness_data.update({(person, 'mkierc'): 0})
        happiness_data.update({('mkierc', person): 0})

    people.add('mkierc')

    return list(people), happiness_data


def solve(raw_data):
    people, happiness_data = parse(raw_data)
    cyclic_permutations = [[people[0], *x] for x in itertools.permutations(people[1:])]

    maximum_happiness = 0

    for permutation in cyclic_permutations:
        total_happiness = 0

        for a, b in zip(permutation, [*permutation[1:], permutation[0]]):
            stat_1 = happiness_data.get((a, b))
            stat_2 = happiness_data.get((b, a))
            total_happiness += stat_1 + stat_2

        if total_happiness > maximum_happiness:
            maximum_happiness = total_happiness

    return maximum_happiness


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    answer = solve(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
