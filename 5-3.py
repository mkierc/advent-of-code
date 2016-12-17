from hashlib import md5

door_id = "uqwqemis"
test_input_1 = "abc"

red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"


def decode(_door_id):
    password = ["_", "_", "_", "_", "_", "_", "_", "_"]
    index = 0

    while "_" in password:
        door_hash = md5(bytes(_door_id + str(index), "utf-8")).hexdigest()
        if door_hash.startswith("00000"):
            try:
                if int(door_hash[5]) in range(8) and password[int(door_hash[5])] == "_":
                    password[int(door_hash[5])] = door_hash[6]
            except ValueError:
                pass

        if index % 100000 == 0:
            eye_candy = list(password)
            for i in range(8):
                if eye_candy[i] == "_":
                    eye_candy[i] = red + door_hash[i] + reset
                else:
                    eye_candy[i] = green + eye_candy[i] + reset
            print("\r" + "".join(eye_candy), end="")

        index += 1

    return "".join(password)


# test_1 = decode(test_input_1)
answer = decode(door_id)

# print("\r" + test_1)
print("\r" + answer)
