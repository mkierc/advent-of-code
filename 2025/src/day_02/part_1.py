import re

range_regex = r'(\d+)-(\d+)'

test_ranges = [(11, 22), (95, 115), (998, 1012), (1188511880, 1188511890), (222220, 222224),
               (1698522, 1698528), (446443, 446449), (38593856, 38593862), (565653, 565659),
               (824824821, 824824827), (2121212118, 2121212124)]

ranges = []

with (open("data.txt") as file):
    line = file.readline()
    ranges = [(int(x), int(y)) for x, y in re.findall(range_regex, line)]


def find_invalid_ids(id_range_list):
    checksum = 0
    for id_range in id_range_list:
        for i in range(id_range[0], id_range[1] + 1):
            if len(str(i)) % 2 == 1:
                continue
            if str(i)[len(str(i)) // 2:len(str(i))] == str(i)[0:len(str(i)) // 2]:
                checksum += i
    return checksum


def main():
    test = find_invalid_ids(test_ranges)
    print("test:", test)

    answer = find_invalid_ids(ranges)
    print("answer:", answer)


if __name__ == "__main__":
    main()
