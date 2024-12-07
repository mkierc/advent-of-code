import itertools
import re
from time import time

levels_regex = r'(\d+)'

test_data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''

test_equations = []

for line in test_data.splitlines():
    a = [int(_) for _ in re.findall(levels_regex, line)]
    test_equations.append(a)

equations = []

with (open("data.txt") as file):
    for line in file.readlines():
        a = [int(_) for _ in re.findall(levels_regex, line)]
        equations.append(a)


def evaluate(equation):
    result = equation[0]

    elements = equation[1:]

    # todo: sort elements of equation to eliminate numbers that get too high quickly
    # elements = sorted(elements, reverse=True)

    operator_combos = []
    # todo: generate once in a separate method with memoization to optimize
    for operator in itertools.combinations_with_replacement(['*', '+'], len(elements)-1):
        for op in set(itertools.permutations(operator)):
            operator_combos.append(op)

    # print(operator_combos)

    # good_ops_count = 0

    for operators in operator_combos:
        current_result = elements[0]
        for i, op in enumerate(operators):
            if current_result > result:
                break
            if op == '*':
                current_result *= elements[i+1]
            if op == '+':
                current_result += elements[i+1]
        if current_result == result:
            return True

    # return good_ops_count


def calibrate(equation_list):
    calibration_result = 0
    for equation in equation_list:
        print(equation)
        if evaluate(equation):
            calibration_result += equation[0]

    return calibration_result


def main():
    test_1 = calibrate(test_equations)
    print("test_1:", test_1)

    start = time()
    answer = calibrate(sorted(equations, reverse=True))
    print(f'time: {time() - start} s')
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer: 6392012777720
# naive brute-force:            1336.7559776306152 s

