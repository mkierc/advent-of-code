import re

levels_regex = r'(\d+)'

test_list_1 = [7, 6, 4, 2, 1]  # Safe because the levels are all decreasing by 1 or 2.
test_list_2 = [1, 2, 7, 8, 9]  # Unsafe because 2 7 is an increase of 5.
test_list_3 = [9, 7, 6, 2, 1]  # Unsafe because 6 2 is a decrease of 4.
test_list_4 = [1, 3, 2, 4, 5]  # Unsafe because 1 3 is increasing but 3 2 is decreasing.
test_list_5 = [8, 6, 4, 4, 1]  # Unsafe because 4 4 is neither an increase or a decrease.
test_list_6 = [1, 3, 6, 7, 9]  # Safe because the levels are all increasing by 1, 2, or 3.

report = []

with (open("data.txt") as file):
    for line in file.readlines():
        a = [int(_) for _ in re.findall(levels_regex, line)]
        report.append(a)


def is_safe(levels):
    diffs = []

    # increasing
    if levels[0] > levels[1]:
        for i in range(len(levels) - 1):
            diffs.append(levels[i] - levels[i + 1])

    # decreasing
    elif levels[0] < levels[1]:
        for i in range(len(levels) - 1):
            diffs.append(levels[i + 1] - levels[i])
    else:
        return False

    for diff in diffs:
        if diff not in [1, 2, 3]:
            return False

    return True


def count_safe(level_list):
    safe_count = 0
    for levels in level_list:
        if is_safe(levels):
            safe_count += 1
    return safe_count


def main():
    test_1 = is_safe(test_list_1)
    print("test_1:", test_1)
    test_2 = is_safe(test_list_2)
    print("test_2:", test_2)
    test_3 = is_safe(test_list_3)
    print("test_3:", test_3)
    test_4 = is_safe(test_list_4)
    print("test_4:", test_4)
    test_5 = is_safe(test_list_5)
    print("test_5:", test_5)
    test_6 = is_safe(test_list_6)
    print("test_6:", test_6)

    answer = count_safe(report)
    print("answer:", answer)


if __name__ == "__main__":
    main()
