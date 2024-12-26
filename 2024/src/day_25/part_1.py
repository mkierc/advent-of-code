from time import time

keys = []
locks = []

with open('data.txt') as file:
    splitted = [x.splitlines() for x in file.read().split('\n\n')]

    for _ in splitted:
        if _[0] == '.....':
            keys.append(_)
        else:
            locks.append(_)


def invert_key_to_lock(key):
    lock = []
    for line in key:
        new_line = ''
        for char in line:
            if char == '.':
                new_line += '#'
            elif char == '#':
                new_line += '.'
        lock.append(new_line)
    return lock


def pair_locks(keys, locks):
    paired_sum = 0
    for key in keys:
        for lock in locks:
            # key does NOT have to match exactly to the lock...
            # if not (lock == invert_key_to_lock(key)):
            match = True
            for i in range(len(lock)):
                for j in range(len(lock[0])):
                    if not ((lock[i][j] == '#' and key[i][j] == '.')
                            or (lock[i][j] == '.' and lock[i][j] == '.')):
                        match = False
                        break
            if match:
                paired_sum += 1
    return paired_sum


def main():
    start = time()
    answer = pair_locks(keys, locks)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
