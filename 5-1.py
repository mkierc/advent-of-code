from hashlib import md5

door_id = "uqwqemis"

test_input_1 = "abc"


def decode(_door_id):
    password = ''
    index = 0

    while len(password) < 8:
        door_hash = md5(bytes(_door_id + str(index), "utf-8")).hexdigest()
        if door_hash.startswith("00000"):
            password += door_hash[5]
            print(door_hash, door_hash[5])
        index += 1

    return password

test_1 = decode(test_input_1)
answer = decode(door_id)

print("test_1:", test_1)
print("answer:", answer)
