test_banks = [
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111',
]

banks = []

with (open("data.txt") as file):
    for line in file.read().splitlines():
        banks.append(line)


def joltage(bank):
    max_a = 0
    for i in range(len(bank) - 1):
        # print(i, bank[i], max_a)
        if int(bank[i]) > int(bank[max_a]):
            max_a = i

    max_b = max_a + 1
    for i in range(max_a + 2, len(bank)):
        # print(i, bank[i], max_b)
        if int(bank[i]) > int(bank[max_b]):
            max_b = i

    # print(bank, 10*int(bank[max_a]) + int(bank[max_b]), max_a, max_b, bank[max_a], bank[max_b])
    return 10 * int(bank[max_a]) + int(bank[max_b])


def calculate_total_joltage(bank_list):
    total_joltage = 0
    for bank in bank_list:
        total_joltage += joltage(bank)
    return total_joltage


def main():
    test = calculate_total_joltage(test_banks)
    print("test:", test)

    answer = calculate_total_joltage(banks)
    print("answer:", answer)


if __name__ == "__main__":
    main()
