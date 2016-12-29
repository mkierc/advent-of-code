import re
from day_07.part_1 import input_data
from day_07.part_1 import test_input_1, test_input_2, test_input_3, test_input_4


def get_abas(sequence):
    # use lookahead assertion (?= ... ) to match overlapping aba sequences, i.e.: zazbz -> zaz, zbz
    aba_regex = re.findall(r"(?=([a-z])([a-z])\1)", sequence)

    # remove invalid aaa sequences
    abas = list(filter(lambda x: x[0] != x[1], aba_regex))

    if len(abas) > 0:
        return abas
    else:
        return False


def supports_ssl(address):
    # split by either '[' or ']',
    sequences = re.split("(?:\[|\])", address)

    # group into hypernet and non-hypernet parts (odd/even sequences in list)
    hypernet = sequences[1::2]
    non_hypernet = sequences[0::2]

    # find abas in non-hypernet sequences
    abas = []
    for sequence in non_hypernet:
        aba = get_abas(sequence)
        if aba:
            abas.extend(aba)

    # find babs in hypernet sequences
    babs = []
    for sequence in hypernet:
        bab = get_abas(sequence)
        if bab:
            babs.extend(bab)

    # invert the character in found babs
    inverted_babs = []
    for bab in babs:
        inverted_babs.append((bab[1], bab[0]))

    # does the intersection of abas set and inverted babs set exist
    if len(set(abas) & set(inverted_babs)) > 0:
        return True
    else:
        return False


def main():
    test_1 = supports_ssl(test_input_1)
    test_2 = supports_ssl(test_input_2)
    test_3 = supports_ssl(test_input_3)
    test_4 = supports_ssl(test_input_4)

    ssl_supported = 0
    for adress in input_data:
        if supports_ssl(adress):
            ssl_supported += 1

    print("test_1:", test_1)
    print("test_2:", test_2)
    print("test_3:", test_3)
    print("test_4:", test_4)
    print("answer:", ssl_supported)

if __name__ == "__main__":
    main()
