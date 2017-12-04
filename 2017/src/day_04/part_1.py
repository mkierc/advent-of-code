test_input_1 = ['aa bb cc dd ee']
test_input_2 = ['aa bb cc dd aa']
test_input_3 = ['aa bb cc dd aaa']

pass_phrases = []

with open("data.txt") as file:
    for line in file:
        pass_phrases.append(line.split())


def validate(phrase):
    existing = set()
    for word in phrase:
        if word not in existing:
            existing.add(word)
        else:
            return False
    return True


def validate_phrases(phrase_list):
    valid_count = 0

    for phrase in phrase_list:
        if validate(phrase):
            valid_count += 1

    return valid_count


def main():
    test_1 = validate(test_input_1)
    test_2 = validate(test_input_2)
    test_3 = validate(test_input_3)
    answer = validate_phrases(pass_phrases)

    print("test_1:", test_1)
    print("test_2:", test_2)
    print("test_3:", test_3)
    print("answer:", answer)


if __name__ == "__main__":
    main()
