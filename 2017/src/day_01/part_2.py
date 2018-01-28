test_list_1 = [1, 2, 1, 2]
test_list_2 = [1, 2, 2, 1]
test_list_3 = [1, 2, 3, 4, 2, 5]
test_list_4 = [1, 2, 3, 1, 2, 3]
test_list_5 = [1, 2, 1, 3, 1, 4, 1, 5]

number_list = []

with open("data.txt") as file:
    input_data = str(file.readline())
    for character in input_data:
        number_list.append(int(character))


def solve_captcha(numbers):
    captcha_sum = 0
    i = 0

    while i < len(numbers):
        a = numbers[i % len(numbers)]
        b = numbers[int((i + (len(numbers) / 2))) % len(numbers)]
        if a == b:
            captcha_sum += a
        i += 1

    return captcha_sum


def main():
    test_1 = solve_captcha(test_list_1)
    print("test_1:", test_1)
    test_2 = solve_captcha(test_list_2)
    print("test_2:", test_2)
    test_3 = solve_captcha(test_list_3)
    print("test_3:", test_3)
    test_4 = solve_captcha(test_list_4)
    print("test_4:", test_4)
    test_5 = solve_captcha(test_list_5)
    print("test_5:", test_5)

    answer = solve_captcha(number_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
