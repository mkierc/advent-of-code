from hashlib import md5

import time

input_data = "uqwqemis"
test_input_1 = "abc"


def decode(door_id):
    password = ""
    index = 0

    while len(password) < 8:
        door_hash = md5(bytes(door_id + str(index), "utf-8")).hexdigest()
        if door_hash.startswith("00000"):
            password += door_hash[5]
            # print(door_hash, door_hash[5])
        index += 1

    return password


def main():
    start = time.time()
    test_1 = decode(test_input_1)
    print("time:", (time.time() - start))
    print("test_1:", test_1)

    start = time.time()
    answer = decode(input_data)
    print("time:", (time.time() - start))
    print("answer:", answer)


if __name__ == "__main__":
    main()
