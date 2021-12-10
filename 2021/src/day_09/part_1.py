test_map = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]

floor_map = []

with open("data.txt") as file:
    for line in file.read().splitlines():
        floor_map.append([int(x) for x in line])


def calculate_risk(_map):
    total_risk = 0
    for i, row in enumerate(_map):
        for j, value in enumerate(row):
            adjacent = []
            if not j == 0:
                adjacent.append(_map[i][j-1])
            if not j == len(row)-1:
                adjacent.append(_map[i][j+1])
            if not i == 0:
                adjacent.append(_map[i-1][j])
            if not i == len(_map) - 1:
                adjacent.append(_map[i+1][j])
            is_low = True
            for a in adjacent:
                if value >= a:
                    is_low = False
                    break
            if is_low:
                total_risk = total_risk + value + 1

    return total_risk


def main():
    test = calculate_risk(test_map)
    print("test:", test)

    answer = calculate_risk(floor_map)
    print("answer:", answer)


if __name__ == "__main__":
    main()
