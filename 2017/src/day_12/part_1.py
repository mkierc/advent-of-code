import re

test_input_1 = [
    '0 <-> 2',
    '1 <-> 1',
    '2 <-> 0, 3, 4',
    '3 <-> 2, 4',
    '4 <-> 2, 3, 6',
    '5 <-> 6',
    '6 <-> 4, 5'
]

with open("data.txt") as file:
    input_data = file.read().split('\n')


def find_group(program_map, found, program_id):
    potential_new_programs = program_map.get(program_id)

    if found.union(potential_new_programs) == found:
        return found

    found = found.union(potential_new_programs)

    for potential in potential_new_programs:
        found = found.union(find_group(program_map, found, potential))

    return found


def group_programs(pipe_list):
    program_map = dict()

    for line in pipe_list:
        regex = re.search('(\d+) <-> ([, \d]+)', line)
        program_id = int(regex.group(1))
        connected = set(int(x) for x in regex.group(2).split(','))
        program_map.update({program_id: connected})

    return len(find_group(program_map, {0}, 0))


def main():
    test_1 = group_programs(test_input_1)
    answer = group_programs(input_data)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
