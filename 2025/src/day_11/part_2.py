from collections import defaultdict
from time import time

test_input = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
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


def find_all_paths_recursive_dfs(edges, start, end):
    edges['out'] = []

    paths = defaultdict(int)
    visited_nodes = defaultdict(bool)

    def dfs(_from, _to):
        visited_nodes[_from] = True

        for node in edges[_from]:
            if node == _to:
                paths[_from] += 1
                continue

            if not visited_nodes[node]:
                dfs(node, _to)

            paths[_from] += paths[node]

    dfs(start, end)
    return paths[start]


def solve(edges):
    svr_to_fft = find_all_paths_recursive_dfs(edges, 'svr', 'fft')
    fft_to_dac = find_all_paths_recursive_dfs(edges, 'fft', 'dac')
    dac_to_out = find_all_paths_recursive_dfs(edges, 'dac', 'out')

    return svr_to_fft * fft_to_dac * dac_to_out


def main():
    test_1 = solve(test_rack)
    print('test_1:', test_1)

    start = time()
    answer = solve(rack)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
