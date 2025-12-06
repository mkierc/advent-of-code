from time import time

test_operators = ['*', '+', '*', '+']
test_numbers = [
    [123, 328, 51, 64],
    [45, 64, 387, 23],
    [6, 98, 215, 314]
]

operators = []
numbers = []

with open('data.txt') as file:
    input_data = file.read().splitlines()
    for i, line in enumerate(input_data):
        if i != len(input_data) - 1:
            line = [int(x) for x in line.split()]
            numbers.append(line)
        else:
            operators = line.split()


def solve(operators, numbers):
    totals = []
    print(operators, numbers)
    for i, operator in enumerate(operators):
        if operator == '+':
            subtotal = 0
            for j in range(len(numbers)):
                subtotal += numbers[j][i]
            totals.append(subtotal)
        elif operator == '*':
            subtotal = 1
            for j in range(len(numbers)):
                subtotal *= numbers[j][i]
            totals.append(subtotal)

    return sum(totals)


def main():
    test_1 = solve(test_operators, test_numbers)
    print('test_1:', test_1)

    start = time()
    answer = solve(operators, numbers)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
