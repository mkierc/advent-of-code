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

        # print(len(cost_to_node), len(next(iter(cost_to_node.keys()))))

        # generate new molecules from rules
        new_molecules = set()
        for rule in ruleset:
            new_molecules.add(current.replace(rule, ruleset[rule][0], 1))

        for new in new_molecules:
            new_cost = cost_to_node[current] + heuristic(current, new)
            if new not in cost_to_node or new_cost < cost_to_node[new]:
                cost_to_node[new] = new_cost
                priority = new_cost + heuristic(goal, new)
                heapq.heappush(priority_queue, (priority, new))
                visited_nodes[new] = current


# real times:
#
# ans   time[s]
# 20    0.07018303871154785
# 25    1.063807725906372
# 30    3.4922823905944824
# 31    9.016967058181763
# 32    15.026941537857056
# 35    62.044997692108154
# 40    158.07415962219238


# predicted by extrapolation:
# def y(x):
#     return 0.8297685200684696 x*x - 42.33438809724625 x + 524.3708598094684
#
# ans   time [s]                time [min]
# 60    971.4742462211839       16.19123743701973
# 100   4588.617250769539       76.47695417949232


# this input is unexpectedly hard to solve...
# 35: 'CRnSiThRnPBCaCaPMgArYTiTiBPRnSiThSiThSiRnFYPMgArRnPTiBFArArFArCaSiThCaSiThRnSiThCaPTiMgAr',


generated_inputs = {
    20: 'CRnSiThSiRnBCaFArFYPMgYPMgArCaPRnCaSiThFArSiThSiThRnFAr',
    25: 'CRnFYMgArSiThSiRnMgArSiRnCaFYCaCaSiThSiRnSiThRnFArArTiBSiThPBFArPTiMg',
    30: 'CRnBFArRnPRnSiThFArSiThCaPBSiRnFArTiBFArSiRnPMgYFArSiRnFArBCaSiRnSiAlArRnSiAlArPMg',
    31: 'CRnPTiRnPBSiThSiAlArSiThSiThCaSiThPMgYTiRnFArSiThRnFArArCaSiRnPMgArTiTiBPBF',
    32: 'CRnSiRnSiAlArTiBCaFYSiThFYSiRnMgArSiRnMgArSiRnPBPMgArBPRnCaFArCaSiAlArSiThSiRnFYSiAlArSiThF',
    35: 'CRnPMgArRnBPRnFArFArPTiTiRnFArSiThSiThSiRnCaPBPMgArTiRnSiRnMgArSiRnFArTiBPMgArPBPRnFArCaF',
    40: 'CRnTiBSiRnFArBPMgYSiRnFYFArCaSiRnSiThFArRnSiRnFYFArSiRnFYFArCaSiThSiThFArSiRnSiThCaFArBPMgArSiRnBPMgArSiRnFArRnFArSiAl',
    60: 'CRnTiTiRnFArPBSiThFYSiThCaPBPTiBSiThSiRnFArMgArPRnFArCaSiRnTiTiRnPMgArCaSiThSiRnSiRnFArMgArBFArSiThSiRnMgArSiThSiRnCaSiRnMgArCaSiRnMgArSiThRnFArArBPTiBSiThRnFAr'
}


def main():
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
