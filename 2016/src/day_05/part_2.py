import time
from hashlib import md5

input_data = "uqwqemis"
test_input_1 = "abc"


def decode(_door_id):
    password = list("________")
    index = 0

    while "_" in password:
        door_hash = md5(bytes(_door_id + str(index), "utf-8")).hexdigest()
        if door_hash.startswith("00000"):
            if door_hash[5].isdigit():
                if int(door_hash[5]) < 8:
                    if password[int(door_hash[5])] == "_":
                        password[int(door_hash[5])] = door_hash[6]
                        print(door_hash, door_hash[5], door_hash[6], password)
        index += 1

    return "".join(password)


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
