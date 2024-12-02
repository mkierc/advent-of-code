import re

location_regex = r'(\d+) *(\d+)'

test_list_a = [3, 4, 2, 1, 3, 3]
test_list_b = [4, 3, 5, 3, 9, 3]

location_list_a = []
location_list_b = []

with (open("data.txt") as file):
    for line in file.readlines():
        a, b = re.findall(location_regex, line)[0]
        location_list_a.append(int(a))
        location_list_b.append(int(b))


def calculate_distance(list_a, list_b):
    assert len(list_a) == len(list_b)
    list_a.sort()
    list_b.sort()
    distance = 0
    for i in range(len(list_a)):
        distance = distance + abs(list_a[i] - list_b[i])
    return distance


def main():
    test = calculate_distance(test_list_a, test_list_b)
    print("test:", test)

    answer = calculate_distance(location_list_a, location_list_b)
    print("answer:", answer)


if __name__ == "__main__":
    main()
