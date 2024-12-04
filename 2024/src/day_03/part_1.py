import re

mul_regex = r'mul\((\d+),(\d+)\)'

report = []

with open("data.txt") as file:
    for line in file.readlines():
        for a, b in re.findall(mul_regex, line):
            report.append((int(a),int(b)))


def calculate(pairs):
    result = 0
    for a, b in pairs:
        result += a * b
    return result


def main():
    answer = calculate(report)
    print("answer: ", answer)


if __name__ == "__main__":
    main()
