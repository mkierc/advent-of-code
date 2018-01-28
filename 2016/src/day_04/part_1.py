import re

test_input_1 = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
]

with open("data.txt") as file:
    input_data = file.read().splitlines()


def is_valid(room):
    """
    if room is authentic:
        returns room_id
    if room is not authentic:
        return 0
    """
    (room_name, room_id, checksum) = re.split("(\d+)", room)
    room_name = room_name.replace("-", "")
    room_id = int(room_id)
    checksum = checksum.replace("[", "").replace("]", "")

    # make a list of tuples containing respectively letters and their counts
    letter_statistics = []
    for letter_count in room_name:
        letter_count = (letter_count, room_name.count(letter_count))
        if letter_count not in letter_statistics:
            letter_statistics.append(letter_count)

    # sort the list of letters respectively by:
    #   -x[1]   count, in reverse order (from highest to lowest):
    #    x[0]   then alphabetically in each count tier
    sorted_letter_stats = sorted(letter_statistics, key=lambda x: (-x[1], x[0]))

    # truncate list to five most common letters
    top_five = ""
    for letter_count in sorted_letter_stats[:5]:
        top_five += letter_count[0]

    if top_five == checksum:
        return room_id
    else:
        return 0


def sum_valid_sector_codes(room_list):
    sector_sum = 0
    for room in room_list:
        sector_sum += is_valid(room)
    return sector_sum


def main():
    test_1 = sum_valid_sector_codes(test_input_1)
    print("test_1:", test_1)

    answer = sum_valid_sector_codes(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
