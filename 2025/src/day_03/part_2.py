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


def twelve_digit_joltage(bank):
    max = [0]

    for digit in range(12):
        for i in range(max[digit], len(bank)-(11-digit)):
            # print(digit, i, bank[i], max)
            if int(bank[i]) > int(bank[max[digit]]):
                max[digit] = i
        if digit < 11:
            max.append(max[digit]+1)

    # print(bank, int(''.join([bank[x] for x in max])), max)
    return int(''.join([bank[x] for x in max]))


def calculate_total_joltage(bank_list):
    total_joltage = 0
    for bank in bank_list:
        total_joltage += twelve_digit_joltage(bank)
    return total_joltage


def main():
    test = calculate_total_joltage(test_banks)
    print("test:", test)

    answer = calculate_total_joltage(banks)
    print("answer:", answer)


if __name__ == "__main__":
    main()
