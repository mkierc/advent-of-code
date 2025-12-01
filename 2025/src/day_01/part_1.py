import re

location_regex = r'(L|R)(\d+)'

test_rotations = [('L', 68),
                  ('L', 30),
                  ('R', 48),
                  ('L', 5),
                  ('R', 60),
                  ('L', 55),
                  ('L', 1),
                  ('L', 99),
                  ('R', 14),
                  ('L', 82)]

rotations = []

with (open("data.txt") as file):
    for line in file.readlines():
        a, b = re.findall(location_regex, line)[0]
        rotations.append((a, int(b)))


def analyze_rotations(rotation_list):
    current_state = 50
    counter = 0
    for a, b in rotation_list:
        if a == 'L':
            current_state -= b
            current_state %= 100
        else:
            current_state += b
            current_state %= 100
        print(current_state)
        if current_state == 0:
            counter += 1
    return counter


def main():
    test = analyze_rotations(test_rotations)
    print("test:", test)

    answer = analyze_rotations(rotations)
    print("answer:", answer)


if __name__ == "__main__":
    main()
