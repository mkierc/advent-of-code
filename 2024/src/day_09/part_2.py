from time import time

test_list = [int(_) for _ in '2333133121414131402']

with open("data.txt") as file:
    data = [int(_) for _ in file.readline()]


def calculate_checksum(disk_map):
    disk = []
    block_index = 0

    for i, count in enumerate(disk_map):
        if i % 2 == 0:
            disk.append((count, block_index))
            block_index += 1
        else:
            disk.append((count, '.'))

    disk_index = 0
    while disk_index < len(disk):
        count = disk[disk_index][0]
        block_index = disk[disk_index][1]

        if block_index == '.':
            free_space = count
            reversed_disk_index = len(disk) - 1

            while reversed_disk_index > disk_index and free_space > 0:
                rev_count = disk[reversed_disk_index][0]
                rev_block_index = disk[reversed_disk_index][1]

                if rev_block_index != '.' and rev_count <= free_space:
                    disk[reversed_disk_index] = (rev_count, '.')
                    disk[disk_index] = (disk[disk_index][0]-rev_count, disk[disk_index][1])
                    free_space -= rev_count
                    disk.insert(disk_index, (rev_count, rev_block_index))
                    disk_index += 1

                reversed_disk_index -= 1

            if free_space == 0:
                del disk[disk_index]

        disk_index += 1

    checksum = 0

    disk_index = 0
    for count, block_index in disk:
        for i in range(count):
            if block_index == '.':
                disk_index += 1
                # print(disk_index, count, block_index, checksum)
            else:
                checksum += disk_index * block_index
                disk_index += 1
                # print(disk_index, count, block_index, i, checksum)

    return checksum


def main():
    test = calculate_checksum(test_list)
    print("test:", test)

    start = time()
    answer = calculate_checksum(data)
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()


# answer: 6421724645083
# without actual writes to disk        6.223328113555908 s
# todo: compare to unoptimized version with actual writes to disk array (use partial prints to determine if it's viable)
