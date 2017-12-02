test_input = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5]
]

input_spreadsheet = []

with open("data.txt") as file:
    for line in file:
        line_chars = line.split()
        line_numbers = []
        for number in line_chars:
            line_numbers.append(int(number))

        input_spreadsheet.append(line_numbers)


def calculate_checksum(spreadsheet):
    spreadsheet_sum = 0

    for row in spreadsheet:
        difference = find_even_divisors(row)
        spreadsheet_sum += difference
    return spreadsheet_sum


def find_even_divisors(row):
    for i in range(len(row)):
        divident = row[i]
        potential_divisors = row[:i] + row[i+1:]
        for potential_divisor in potential_divisors:
            if divident / potential_divisor == divident // potential_divisor:
                return divident // potential_divisor


def main():
    test_1 = calculate_checksum(test_input)
    answer = calculate_checksum(input_spreadsheet)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
