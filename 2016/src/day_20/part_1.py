with open("data.txt") as file:
    input_data = []
    for line in file.readlines():
        a, b = line.split("-")
        input_data.append((int(a), int(b)))


def main():
    blacklist = sorted(input_data, key=lambda x: x[0])

    lowest_ip = 0
    for ip in blacklist:
        if lowest_ip in range(ip[0], ip[1]):
            lowest_ip = ip[1] + 1

    print("answer:", lowest_ip)


if __name__ == "__main__":
    main()
