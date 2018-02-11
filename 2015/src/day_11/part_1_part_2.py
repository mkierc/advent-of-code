test_input_1 = 'hijklmmn'
test_input_2 = 'abbceffg'
test_input_3 = 'abbcegjk'

test_input_4 = 'abcdefgh'
test_input_5 = 'ghijklmn'

input_data = 'cqjxjnds'


# full alphabet
full_alphabet = 'abcdefghijklmnopqrstuvwxyz'

# the alphabet without 'i', 'l' and 'o' letters
valid_alphabet = 'abcdefghjkmnpqrstuvwxyz'

# list of consecutive triplets ['abc', 'bcd', ...]
triplets = [a + b + c for a, b, c in zip(full_alphabet, full_alphabet[1:], full_alphabet[2:])]

# list of tuplets ['aa', 'bb', 'cc', ...]
tuplets = [a + a for a in full_alphabet]


def validate_password(password, test=False):
    # no need to use the "no i/l/o" rule in real case, because I don't generate passwords with those letters
    if test and ('i' in password or 'l' in password or 'o' in password):
        return False

    # check if password contain any of the triplets
    has_triplet = False

    for triplet in triplets:
        if triplet in password:
            has_triplet = True

    if not has_triplet:
        return False

    # check if password contains at least two tuplets
    tuplet_count = 0

    for tuplet in tuplets:
        if tuplet in password:
            tuplet_count += 1

    if tuplet_count < 2:
        return False

    return True


def next_character(character):
    # only for test cases
    if character == 'i':
        return 'j'
    elif character == 'l':
        return 'm'
    elif character == 'o':
        return 'p'

    # return the next letter, wrap around to 'a' if 'z'
    return valid_alphabet[(valid_alphabet.index(character) + 1) % len(valid_alphabet)]


def generate_next_candidate(password):
    prefix = password.rstrip('z')
    suffix_size = len(password) - len(prefix)

    if prefix:
        new_suffix = prefix[:-1] + next_character(prefix[-1])
    else:
        new_suffix = 'a'

    new_suffix += 'a' * suffix_size

    return new_suffix


def find_next_password(password, test=False):
    password = generate_next_candidate(password)

    while not validate_password(password, test):
        password = generate_next_candidate(password)

    return password


def main():
    test_1 = validate_password(test_input_1, test=True)
    print('test_1:', test_1)

    test_2 = validate_password(test_input_2, test=True)
    print('test_2:', test_2)

    test_3 = validate_password(test_input_3, test=True)
    print('test_3:', test_3)

    test_4 = find_next_password(test_input_4, test=True)
    print('test_4:', test_4)

    test_5 = find_next_password(test_input_5, test=True)
    print('test_5:', test_5)

    part_1 = find_next_password(input_data)
    print('part_1:', part_1)

    part_2 = find_next_password(part_1)
    print('part_2:', part_2)


if __name__ == '__main__':
    main()
