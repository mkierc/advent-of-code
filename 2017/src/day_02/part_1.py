test_input = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
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
        difference = find_extremes_difference(row)
        spreadsheet_sum += difference
    return spreadsheet_sum


def find_extremes_difference(row):
    lowest = row[0]
    highest = row[0]
    for number in row:
        if number < lowest:
            lowest = number
        if number > highest:
            highest = number
    return highest - lowest


def main():
    test_1 = calculate_checksum(test_input)
    print("test_1:", test_1)

    answer = calculate_checksum(input_spreadsheet)
    print("answer:", answer)


if __name__ == "__main__":
    main()
