from day_06.part_1 import input_data
from day_06.part_1 import test_input_1


def decode(message):
    transposed_message = list(zip(*message))
    decoded = ""

    # find the most common character in each group
    for char_group in transposed_message:
        ranking = set()
        for char in char_group:
            ranking.add((char, char_group.count(char)))
        decoded += min(ranking, key=lambda x: x[1])[0]

    return decoded


def main():
    test_1 = decode(test_input_1)
    answer = decode(input_data)

    print("test_1:", test_1)
    print("answer:", answer)

if __name__ == "__main__":
    main()
