import re
from day_04.part_1 import input_data
from day_04.part_1 import is_valid

ASCII_OFFSET = 97
test_input_2 = "qzmt-zixmtkozy-ivhz-343"


def decipher_name(room):
    (name, number, checksum) = re.split("(\d+)", room)

    decoded = ""
    for letter in name:
        if ord(letter) == 45:
            decoded += " "
        else:
            decoded += chr(((ord(letter) - ASCII_OFFSET + int(number)) % 26) + ASCII_OFFSET)

    return decoded


def find_north_pole_objects(rooms):
    valid_rooms = []

    for room in rooms:
        valid_id = is_valid(room)
        if valid_id:
            deciphered = decipher_name(room)
            valid_rooms.append((deciphered, valid_id))

    for room in valid_rooms:
        if "north" in room[0]:
            return room[0], room[1]


def main():
    test_2 = decipher_name(test_input_2)
    answer = find_north_pole_objects(input_data)

    print("test_1:", test_2)
    print("answer:", answer)


if __name__ == "__main__":
    main()
