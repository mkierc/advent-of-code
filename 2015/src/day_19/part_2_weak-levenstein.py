import re
from collections import defaultdict
from time import time

test_rules = {
    'H': ['e'],
    'O': ['e'],
    'HO': ['H'],
    'OH': ['H'],
    'HH': ['O']
}

test_input_1 = 'HOH'
test_input_2 = 'HOHOHO'

with open('data.txt') as file:
    input_data = file.read().splitlines()

    # create ruleset
    input_ruleset = defaultdict(list)
    for line in input_data[:-2]:
        a, b = re.match(r'([A-Za-z]+) => ([A-Za-z]+)', line).groups()
        input_ruleset[b].append(a)

    # get result molecule
    input_molecule = input_data[-1]


# levenstein distance has too high computational complexity, so it's pretty much useless :(
def levenstein(molecule_1, molecule_2):
    if not molecule_1:
        return len(molecule_2)
    if not molecule_2:
        return len(molecule_1)
    return min(
        levenstein(molecule_1[1:], molecule_2[1:]) + (molecule_1[0] != molecule_2[0]),
        levenstein(molecule_1[1:], molecule_2) + 1,
        levenstein(molecule_1, molecule_2[1:]) + 1
    )


def simple_heuristic(molecule_1, molecule_2):
    return abs(len(molecule_1) - len(molecule_2))


# very bad implementation of A*-search based on wikipedia pseudocode: https://en.wikipedia.org/wiki/A*_search_algorithm
def a_star_search(ruleset, start):
    def reconstruct_path(came_from: defaultdict, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)
        return total_path

    goal = 'e'

    closed_set = set()
    open_set = {start}

    came_from = {}

    g_scores = defaultdict(lambda: 999_999_999)
    g_scores[start] = 0

    f_scores = defaultdict(lambda: 999_999_999)
    f_scores[start] = simple_heuristic(start, goal)

    while open_set:
        # pick a node that has the lowest f_score from open set
        lowest_score = 999_999_999
        current = ''
        for node in open_set:
            if f_scores[node] < lowest_score:
                lowest_score = f_scores[node]
                current = node

        if current == goal:
            return len(reconstruct_path(came_from, current)) - 1

        open_set.remove(current)
        closed_set.add(current)

        new_molecules = set()
        for rule in ruleset:
            new_molecules.add(current.replace(rule, ruleset[rule][0], 1))

        # print(new_molecules)
        # print(len(open_set), len(closed_set))

        for new_molecule in new_molecules:
            if new_molecule in closed_set:
                continue

            if new_molecule not in open_set:
                open_set.add(new_molecule)

            new_g_score = g_scores[current] + simple_heuristic(current, new_molecule)
            if new_g_score >= g_scores[new_molecule]:
                continue

            came_from[new_molecule] = current
            g_scores[new_molecule] = new_g_score
            f_scores[new_molecule] = g_scores[new_molecule] + simple_heuristic(new_molecule, goal)

    return 'Solution does not exist :('


# real times:
#
# ans   time [s]
# 20    0.3098437786102295
# 21    1.7957541942596436
# 22    8.281009674072266
# 23    16.58006978034973


# predicted by extrapolation:
# def y(x):
#     return 1.703287422657012 x*x - 67.71176582574842 x + 673.0709142088888
#
# ans   time [s]                time [min]
# 30    174.67661982774684      2.911276997129114
# 60    2742.199686229226       45.70332810382043
# 100   10934.768558204165      182.2461426367361


generated_inputs = {
    20: 'CRnCaPBFArRnTiBFArSiRnFYFArPBSiRnPRnFArSiThSiAlYPMgArF',
    21: 'CRnPMgArRnSiRnFArTiRnFArPTiBCaPTiTiTiMgArTiTiBSiThF',
    22: 'CRnSiRnFArTiRnFArSiThRnCaSiAlArYSiRnCaSiThRnFArArTiBCaSiRnFArMgArTiBF',
    23: 'HSiRnFYFArPRnCaFArSiThPBCaCaSiThRnSiRnTiRnFArPTiBFArSiThFAr',
}


def main():
    test_1 = a_star_search(test_rules, test_input_1)
    print('test_1:', test_1)
    test_2 = a_star_search(test_rules, test_input_2)
    print('test_2:', test_2)

    for substitutions, molecule in generated_inputs.items():
        start = time()
        answer = a_star_search(input_ruleset, molecule)
        print(substitutions, answer, time() - start)

    start = time()
    answer = a_star_search(input_ruleset, input_molecule)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
