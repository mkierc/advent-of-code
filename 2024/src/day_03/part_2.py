import re

mul_regex = r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"

report = []

with open("data.txt") as file:
    for line in file.readlines():
        for a, b, c, d in re.findall(mul_regex, line):
            if a and b:
                report.append((int(a), int(b)))
            elif c:
                report.append(c)
            elif d:
                report.append(d)


def calculate(data):
    result = 0
    enabled = True
    for line in data:
        if line == "do()":
            enabled = True
        elif line == "don't()":
            enabled = False
        else:
            a, b = line
            if enabled:
                result += a * b
    return result


def main():
    answer = calculate(report)
    print("answer: ", answer)


if __name__ == "__main__":
    main()
