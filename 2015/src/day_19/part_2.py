import heapq
import re
from collections import defaultdict
from time import time

with open('data.txt') as file:
    input_data = file.read().splitlines()

    # create ruleset
    input_ruleset = defaultdict(list)
    for line in input_data[:-2]:
        a, b = re.match(r'([A-Za-z]+) => ([A-Za-z]+)', line).groups()
        input_ruleset[b].append(a)

    # get result molecule
    input_molecule = input_data[-1]


def a_star_search(ruleset, start):
    def heuristic(molecule_1, molecule_2):
        return abs(len(molecule_1) - len(molecule_2))

    goal = 'e'

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited_nodes = defaultdict(int)
    cost_to_node = defaultdict(int)

    visited_nodes[start] = None
    cost_to_node[start] = 0

    while priority_queue:
        current = heapq.heappop(priority_queue)[1]

        if current == goal:
            # retrace the steps of path
            total_path = [current]
            while current in visited_nodes.keys():
                current = visited_nodes[current]
                total_path.append(current)

            # return size minus 2 (first and last step are **not** molecule replaces)
            return len(total_path) - 2

        # generate new molecules from rules
        new_molecules = set()
        for rule in ruleset:
            new_molecules.add(current.replace(rule, ruleset[rule][0], 1))

        for new in new_molecules:
            # no need to calculate the cost from current to next by heuristic...
            # new_cost = cost_to_node[current] + heuristic(current, new)

            # ...I know the distance, IT'S ONE!
            new_cost = cost_to_node[current] + 1

            if new not in cost_to_node or new_cost < cost_to_node[new]:
                cost_to_node[new] = new_cost
                priority = new_cost + heuristic(goal, new)
                heapq.heappush(priority_queue, (priority, new))
                visited_nodes[new] = current


generated_inputs = {
    '20': 'CRnSiThSiRnBCaFArFYPMgYPMgArCaPRnCaSiThFArSiThSiThRnFAr',
    '25': 'CRnFYMgArSiThSiRnMgArSiRnCaFYCaCaSiThSiRnSiThRnFArArTiBSiThPBFArPTiMg',
    '30': 'CRnBFArRnPRnSiThFArSiThCaPBSiRnFArTiBFArSiRnPMgYFArSiRnFArBCaSiRnSiAlArRnSiAlArPMg',
    '31': 'CRnPTiRnPBSiThSiAlArSiThSiThCaSiThPMgYTiRnFArSiThRnFArArCaSiRnPMgArTiTiBPBF',
    '32': 'CRnSiRnSiAlArTiBCaFYSiThFYSiRnMgArSiRnMgArSiRnPBPMgArBPRnCaFArCaSiAlArSiThSiRnFYSiAlArSiThF',
    '35': 'CRnPMgArRnBPRnFArFArPTiTiRnFArSiThSiThSiRnCaPBPMgArTiRnSiRnMgArSiRnFArTiBPMgArPBPRnFArCaF',
    # this generated input is unexpectedly hard to solve...
    '35*++': 'CRnSiThRnPBCaCaPMgArYTiTiBPRnSiThSiThSiRnFYPMgArRnPTiBFArArFArCaSiThCaSiThRnSiThCaPTiMgAr',
    '40': 'CRnTiBSiRnFArBPMgYSiRnFYFArCaSiRnSiThFArRnSiRnFYFArSiRnFYFArCaSiThSiThFArSiRnSiThCaFArBPMgArSiRnBPMgArSiRnFArRnFArSiAl',
    '60': 'CRnTiTiRnFArPBSiThFYSiThCaPBPTiBSiThSiRnFArMgArPRnFArCaSiRnTiTiRnPMgArCaSiThSiRnSiRnFArMgArBFArSiThSiRnMgArSiThSiRnCaSiRnMgArCaSiRnMgArSiThRnFArArBPTiBSiThRnFAr'
}


def main():
    print('expect'.ljust(6), 'found'.ljust(6), 'time [s]')
    for substitutions, molecule in generated_inputs.items():
        start = time()
        answer = a_star_search(input_ruleset, molecule)
        print(str(substitutions).ljust(6), str(answer).ljust(6), time() - start)

    start = time()
    answer = a_star_search(input_ruleset, input_molecule)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
