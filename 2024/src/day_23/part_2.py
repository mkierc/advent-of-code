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


def find_largest_network(connections):
    nodes_to_networks = defaultdict(set)

    for a, b in connections:
        nodes_to_networks.update({a: {*nodes_to_networks[a], b}})
        nodes_to_networks.update({b: {*nodes_to_networks[b], a}})

    networks = set()

    for i, (k, v) in enumerate(nodes_to_networks.items()):
        print(f'\r{i}/{len(nodes_to_networks)} ', end='')
        for n in range(len(v), 1, -1):
            for combination in itertools.combinations(v, n):
                is_subnet = True
                for a, b in itertools.combinations(combination, 2):
                    if a not in nodes_to_networks[b]:
                        is_subnet = False
                        break
                if is_subnet:
                    networks.add(tuple(sorted({*combination, k})))
                    break  # break if we already found the biggest subnet, we don't need all of them

    # print(networks)
    return ','.join(max(networks, key=lambda x: len(x)))


def main():
    test_1 = find_largest_network(test_connections)
    print("\ntest_1:", test_1)

    start = time()
    answer = find_largest_network(connections)
    print('\ntime:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer:                       bg,bl,ch,fn,fv,gd,jn,kk,lk,pv,rr,tb,vw
# brute-force combo search      4.4381630420684814 s
# break early if found          0.2144272327423095 s
