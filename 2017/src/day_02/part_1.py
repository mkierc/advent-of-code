test_input = [
    ['5', '1', '9', '5'],
    ['7', '5', '3'],
    ['2', '4', '6', '8']
]

input_spreadsheet = []

with open("data.txt") as file:
    for line in file:
        line_numbers = line.split()
        input_spreadsheet.append(line_numbers)


def calculate_checksum(spreadsheet):
    spreadsheet_sum = 0

    for row in spreadsheet:
        difference = find_extremes_difference(row)
        spreadsheet_sum += difference
    return spreadsheet_sum


def find_extremes_difference(row):
    lowest = int(row[0])
    highest = int(row[0])
    for number in row:
        if int(number) < lowest:
            lowest = int(number)
        if int(number) > highest:
            highest = int(number)
    return highest - lowest


def main():
    test_1 = calculate_checksum(test_input)
    answer = calculate_checksum(input_spreadsheet)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
