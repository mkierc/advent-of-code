import itertools
import re
from collections import defaultdict
from time import time

test_connections = [
    ('kh', 'tc'),
    ('qp', 'kh'),
    ('de', 'cg'),
    ('ka', 'co'),
    ('yn', 'aq'),
    ('qp', 'ub'),
    ('cg', 'tb'),
    ('vc', 'aq'),
    ('tb', 'ka'),
    ('wh', 'tc'),
    ('yn', 'cg'),
    ('kh', 'ub'),
    ('ta', 'co'),
    ('de', 'co'),
    ('tc', 'td'),
    ('tb', 'wq'),
    ('wh', 'td'),
    ('ta', 'ka'),
    ('td', 'qp'),
    ('aq', 'cg'),
    ('wq', 'ub'),
    ('ub', 'vc'),
    ('de', 'ta'),
    ('wq', 'aq'),
    ('wq', 'vc'),
    ('wh', 'yn'),
    ('ka', 'de'),
    ('kh', 'ta'),
    ('co', 'tc'),
    ('wh', 'qp'),
    ('tb', 'vc'),
    ('td', 'yn'),
]

connections = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        a, b = re.findall(r'([a-z]+)-([a-z]+)', line)[0]
        connections.append((a, b))


def find_networks(connections, query):
    nodes_to_networks = defaultdict(set)

    for a, b in connections:
        nodes_to_networks.update({a: (*nodes_to_networks[a], b)})
        nodes_to_networks.update({b: (*nodes_to_networks[b], a)})

    three_node_networks = set()

    for k, v in nodes_to_networks.items():
        if len(v) >= 3:
            for b, c in itertools.combinations(v, 2):
                # print(b, c)
                if c in nodes_to_networks[b] and k[0] == query:
                    three_node_networks.add(tuple(sorted((k, b, c))))

    # print(sorted(three_node_networks), len(three_node_networks))

    return len(three_node_networks)


def main():
    test_1 = find_networks(test_connections, 't')
    print("test_1:", test_1)

    start = time()
    answer = find_networks(connections, 't')
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer:   1238
# time:     0.011967658996582031 s
