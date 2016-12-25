from hashlib import md5

door_id = "uqwqemis"

test_input_1 = "abc"


def decode(_door_id):
    password = ["_", "_", "_", "_", "_", "_", "_", "_"]
    index = 0

    while "_" in password:
        door_hash = md5(bytes(_door_id + str(index), "utf-8")).hexdigest()
        if door_hash.startswith("00000"):
            try:
                if int(door_hash[5]) in range(8) and password[int(door_hash[5])] == "_":
                    password[int(door_hash[5])] = door_hash[6]
                    print(door_hash, door_hash[5], door_hash[6], password)
            except ValueError:
                pass
        index += 1

    return "".join(password)

# test_1 = decode(test_input_1)
answer = decode(door_id)

# print("test_1:", test_1)
print("answer:", answer)
