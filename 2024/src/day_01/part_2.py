import re
from collections import defaultdict

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


def calculate_similarity(list_a, list_b):
    assert len(list_a) == len(list_b)

    similarity = defaultdict(lambda: 0)
    counts = defaultdict(lambda: 0)

    for i in range(len(list_b)):
        counts[list_b[i]] = counts[list_b[i]] + 1

    for i in range(len(list_a)):
        similarity[list_a[i]] = similarity[list_a[i]] + list_a[i] * counts[list_a[i]]

    similarity_score = 0

    for value in similarity.values():
        similarity_score = similarity_score + value

    return similarity_score


def main():
    test = calculate_similarity(test_list_a, test_list_b)
    print("test:", test)

    answer = calculate_similarity(location_list_a, location_list_b)
    print("answer:", answer)


if __name__ == "__main__":
    main()
