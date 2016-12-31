from day_20.part_1 import input_data

IP_COUNT = 4294967296  # MAX_INT + 1


def are_mergable(ip_a, ip_b):
    if ip_a[0] >= ip_b[0] >= ip_a[1] \
            or ip_a[0] <= ip_b[1] <= ip_a[1] \
            or ip_b[0] >= ip_a[0] >= ip_b[1] \
            or ip_b[0] <= ip_a[1] <= ip_b[1]:
        return True


def merge(ip_a, ip_b):
    return min(ip_a[0], ip_a[1], ip_b[0], ip_b[1]), max(ip_a[0], ip_a[1], ip_b[0], ip_b[1])


def main():
    blacklist = sorted(input_data, key=lambda x: x[0])

    range_index = 0
    while range_index < len(blacklist):
        try:
            if are_mergable(blacklist[range_index], blacklist[range_index + 1]):
                new_range = merge(blacklist[range_index], blacklist[range_index + 1])
                blacklist[range_index] = new_range
                del blacklist[range_index + 1]
            else:
                range_index += 1
        except IndexError:
            pass
            range_index += 1

    blacklist = sorted(blacklist, key=lambda x: x[0])

    blocked_sum = 0
    for ip in blacklist:
        blocked_sum += ip[1] - ip[0] + 1
    anwser = IP_COUNT - blocked_sum

    print("answer:", anwser)

if __name__ == "__main__":
    main()
