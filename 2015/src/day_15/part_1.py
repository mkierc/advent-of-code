import re

import time

test_input_1 = [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
]

cookie_regex = re.compile(r'([A-Za-z]+): capacity (-?\d+), durability (-?\d+), '
                          r'flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

with open('data.txt') as file:
    input_data = file.read().splitlines()


def parse(raw_data):
    ingredients = []

    for line in raw_data:
        name, capacity, durability, flavor, texture, calories = re.match(cookie_regex, line).groups()
        ingredients.append((name, int(capacity), int(durability), int(flavor), int(texture), int(calories)))

    return ingredients


def solve(raw_data, test=False):
    ingredients = parse(raw_data)

    max_score = 0

    if test:
        for i in range(0, 100):
            for j in range(0, 100):
                if i + j == 100:
                    capacity = 0
                    durability = 0
                    flavor = 0
                    texture = 0

                    capacity += ingredients[0][1] * i
                    durability += ingredients[0][2] * i
                    flavor += ingredients[0][3] * i
                    texture += ingredients[0][4] * i

                    capacity += ingredients[1][1] * j
                    durability += ingredients[1][2] * j
                    flavor += ingredients[1][3] * j
                    texture += ingredients[1][4] * j

                    if capacity < 0:
                        capacity = 0
                    if durability < 0:
                        durability = 0
                    if flavor < 0:
                        flavor = 0
                    if texture < 0:
                        texture = 0

                    score = capacity * durability * flavor * texture

                    if score > max_score:
                        max_score = score
    else:  # TODO optimize the loops
        for i in range(0, 100):
            for j in range(0, 100):
                for k in range(0, 100):
                    for l in range(0, 100):
                        if i + j + k + l == 100:
                            capacity = 0
                            durability = 0
                            flavor = 0
                            texture = 0

                            capacity += ingredients[0][1] * i
                            durability += ingredients[0][2] * i
                            flavor += ingredients[0][3] * i
                            texture += ingredients[0][4] * i

                            capacity += ingredients[1][1] * j
                            durability += ingredients[1][2] * j
                            flavor += ingredients[1][3] * j
                            texture += ingredients[1][4] * j

                            capacity += ingredients[2][1] * k
                            durability += ingredients[2][2] * k
                            flavor += ingredients[2][3] * k
                            texture += ingredients[2][4] * k

                            capacity += ingredients[3][1] * l
                            durability += ingredients[3][2] * l
                            flavor += ingredients[3][3] * l
                            texture += ingredients[3][4] * l

                            if capacity < 0:
                                capacity = 0
                            if durability < 0:
                                durability = 0
                            if flavor < 0:
                                flavor = 0
                            if texture < 0:
                                texture = 0

                            score = capacity * durability * flavor * texture

                            if score > max_score:
                                max_score = score

    return max_score


def main():
    test_1 = solve(test_input_1, True)
    print('test_1:', test_1)

    start = time.time()
    answer = solve(input_data)
    print('time:', time.time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
