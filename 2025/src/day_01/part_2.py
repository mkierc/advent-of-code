import re

code_regex = r'(L|R)(\d+)'

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
        a, b = re.findall(code_regex, line)[0]
        rotations.append((a, int(b)))


def analyze_rotations_method_b(rotation_list):
    current_state = 50
    counter = 0
    for a, b in rotation_list:
        for _ in range(b):
            if a == 'L':
                current_state -= 1
            else:
                current_state += 1
            current_state %= 100
            if current_state == 0:
                counter += 1
    return counter


def main():
    test = analyze_rotations_method_b(test_rotations)
    print("test:", test)

    answer = analyze_rotations_method_b(rotations)
    print("answer:", answer)


if __name__ == "__main__":
    main()
