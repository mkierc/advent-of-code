import heapq
from collections import defaultdict
from time import time

test_input = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
'''

test_rack = dict()
for line in test_input.splitlines():
    _from, to = line.split(': ')
    test_rack.update({_from: to.split()})

rack = dict()
with open('data.txt') as file:
    for line in file.readlines():
        _from, to = line.split(': ')
        rack.update({_from: to.split()})


def find_all_paths(edges):
    start = 'you'
    end = 'out'

    queue = []
    heapq.heappush(queue, start)

    visited_nodes = defaultdict(set)
    cost_to_node = defaultdict(lambda: 0)

    visited_nodes[start] = set()
    cost_to_node[start] = 0

    while queue:
        current = heapq.heappop(queue)

        next_nodes = edges[current]

        for node in next_nodes:
            new_cost = cost_to_node[current] + 1

            if node not in cost_to_node or new_cost < cost_to_node[node]:
                cost_to_node[node] = new_cost

                if node != 'out':
                    heapq.heappush(queue, node)
                visited_nodes[node] = {current}
            elif new_cost == cost_to_node[node]:
                visited_nodes[node] = {*visited_nodes[node], current}

    # retrace the steps of all the equally best paths
    backtrace_queue = []
    heapq.heappush(backtrace_queue, [end])

    list_of_paths = []

    while backtrace_queue:
        current = heapq.heappop(backtrace_queue)
        tail = current[-1]

        # we've found a complete path
        if tail == start:
            list_of_paths.append(current)

        new_tails = visited_nodes[tail]
        for new_tail in new_tails:
            heapq.heappush(backtrace_queue, [*current, new_tail])

    # pprint(list_of_paths)
    return len(list_of_paths)


def main():
    test_1 = find_all_paths(test_rack)
    print('test_1:', test_1)

    start = time()
    answer = find_all_paths(rack)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
