import random
import string
from hashlib import md5
from day_05.part_1 import input_data

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# TODO parallelize hash generation
# TODO use another thread for printing, based on timing instead of index number
# TODO use ncurses to reprint instead of \r
# TODO print pretty output with hashes like in day_05.part_2


def decode(door_id):
    password = list("________")
    index = 0

    while "_" in password:
        door_hash = md5(bytes(door_id + str(index), "utf-8")).hexdigest()
        if door_hash.startswith("00000"):
            if door_hash[5].isdigit():
                if int(door_hash[5]) < 8:
                    if password[int(door_hash[5])] == "_":
                        password[int(door_hash[5])] = door_hash[6]

        # cinematic "decrypting" animation.
        if index % 100000 == 0:
            eye_candy = ""
            decrypted = list(password)
            for letter in decrypted:
                if letter == "_":
                    eye_candy += RED + random.choice(string.hexdigits[:16])
                else:
                    eye_candy += GREEN + letter
            print("\r" + eye_candy, end="")

        index += 1

    return "".join(password)


def main():
    answer = decode(input_data)
    print(RESET, "answer:", answer)

if __name__ == "__main__":
    main()
