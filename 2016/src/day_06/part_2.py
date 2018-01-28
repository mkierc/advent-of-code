test_input_1 = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar"
]

with open("data.txt") as file:
    input_data = file.read().splitlines()


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
    print("test_1:", test_1)

    answer = decode(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
