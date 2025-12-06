from time import time

from numpy import transpose

test_numbers =[
'123 328  51 64 ',
' 45 64  387 23 ',
'  6 98  215 314',
'*   +   *   +  ',
]


with open('data.txt') as file:
    numbers = file.read().splitlines()


def transpose(numbers):
    transposed = list(map(list, zip(*numbers)))

    # add the last empty line, so the loop adds subtotal to total
    transposed.append([' ' for x in range(len(transposed[0]))])

    return transposed


def solve(numbers):
    numbers = transpose(numbers)
    current_operator = ''
    total = 0
    subtotal = 0

    for line in numbers:
        if line[-1] == '+':
            subtotal = 0
            current_operator = '+'
        elif line[-1] == '*':
            subtotal = 1
            current_operator = '*'
        elif set(line) == {' '} or set(line) == {'\n'}:
            total += subtotal
            # print(line, total)
            continue

        number = int(''.join(line[:-1]))
        # print(line, subtotal, current_operator, number)
        if current_operator == '+':
            subtotal += number
        elif current_operator == '*':
            subtotal *= number

    return total


def main():
    test_1 = solve(test_numbers)
    print('test_1:', test_1)

    start = time()
    answer = solve(numbers)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
