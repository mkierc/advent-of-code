import re

password_regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'

test_list = [
    [1, 3, 'a', 'abcde'],
    [1, 3, 'b', 'cdefg'],
    [2, 9, 'c', 'ccccccccc'],
]

password_list = []

with open("data.txt") as file:
    for line in file.readlines():
        password_list.append(*re.findall(password_regex, line))


def count_passwords(password_list):
    correct_list = []

    for password_set in password_list:
        min, max, letter, password = password_set
        if int(min) <= password.count(letter) <= int(max):
            correct_list.append(password)

    return len(correct_list)


def main():
    test = count_passwords(test_list)
    print("test:", test)

    answer = count_passwords(password_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
