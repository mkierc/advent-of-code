import re

with open("data.txt") as file:
    input_data = file.read().splitlines()

test_input_1 = "abba[mnop]qrst"
test_input_2 = "abcd[bddb]xyyx"
test_input_3 = "aaaa[qwer]tyui"
test_input_4 = "ioxxoj[asdfgh]zxcvbn"


def is_abba(sequence):
    abba_regex = re.search(r"([a-z])([a-z])\2\1", sequence)
    if abba_regex:
        if abba_regex.groups()[0] != abba_regex.groups()[1]:
            return True
        else:
            return False
    else:
        return False


def supports_tls(address):
    # split by either '[' or ']',
    sequences = re.split("(?:\[|\])", address)

    # group into hypernet and non-hypernet parts (odd/even sequences in list)
    hypernet = sequences[1::2]
    non_hypernet = sequences[0::2]

    for sequence in hypernet:
        if is_abba(sequence):
            return False

    for sequence in non_hypernet:
        if is_abba(sequence):
            return True
    else:
        return False


def main():
    test_1 = supports_tls(test_input_1)
    test_2 = supports_tls(test_input_2)
    test_3 = supports_tls(test_input_3)
    test_4 = supports_tls(test_input_4)

    tls_supported = 0
    for adress in input_data:
        if supports_tls(adress):
            tls_supported += 1

    print("test_1:", test_1)
    print("test_2:", test_2)
    print("test_3:", test_3)
    print("test_4:", test_4)
    print("answer:", tls_supported)

if __name__ == "__main__":
    main()
