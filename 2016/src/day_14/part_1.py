import re
from hashlib import md5

input_data = "ahsbgdzn"
test_input_1 = "abc"


def uberhash(salt, stretch):
    uber_hash = salt
    for i in range(stretch):
        uber_hash = md5(bytes(uber_hash, "utf-8")).hexdigest()
    return uber_hash


def generate_pad(salt, show_progress=0, stretch=1):
    index = 0
    possible_keys = {}
    true_keys = []

    while len(true_keys) < 64:
        pad_hash = uberhash(salt + str(index), stretch)
        triplet = re.search(r"([a-z0-9])\1\1", pad_hash)
        quintiplet = re.search(r"([a-z0-9])\1\1\1\1", pad_hash)

        to_remove = set()
        if quintiplet:
            number = quintiplet.groups()[0]
            for i in possible_keys:
                if possible_keys[i][1] == number:
                    true_keys.append((i, possible_keys[i][0]))
                    to_remove.add(i)
        elif triplet:
            number = triplet.groups()[0]
            possible_keys.update({index: (pad_hash, number)})

        for i in possible_keys:
            if i < index - 1000:
                to_remove.add(i)
        for i in to_remove:
            possible_keys.pop(i)

        if show_progress and index % 31 == 0:
            print("\rChecked", index, "hashes, found", len(true_keys), "keys.", flush=True, end="")
        index += 1

    if show_progress:
        print("\rChecked", index, "hashes, found all 64 keys.", flush=True)
    # truncating to 64 because this method may confirm more possible keys per quintiplet
    true_keys = sorted(true_keys)[:64]
    return true_keys[-1][0]


def main():
    test_1 = generate_pad(test_input_1)
    print("test_1:", test_1)

    answer = generate_pad(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
