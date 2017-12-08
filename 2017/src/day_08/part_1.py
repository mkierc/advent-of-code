import re

test_input_1 = [
    'b inc 5 if a > 1',
    'a inc 1 if b < 5',
    'c dec -10 if a >= 1',
    'c inc -20 if c == 10'
]

with open("data.txt") as file:
    input_data = file.read().split('\n')


def execute(instructions):
    instruction_list = []
    registers = dict()

    for line in instructions:
        regex = re.search('([a-z]+) ([a-z]+) ([-0-9]+) if ([a-z]+) ([!<>=]+) ([-0-9]+)', line)

        register = regex.group(1)  # a
        operator = regex.group(2)  # inc
        value = int(regex.group(3))  # 5

        condition_register = regex.group(4)  # a
        condition_operator = regex.group(5)  # >
        condition_value = int(regex.group(6))  # 1

        instruction_list.append([register, operator, value, condition_register, condition_operator, condition_value])
        registers.update({register: 0})
        registers.update({condition_register: 0})

    for instruction in instruction_list:
        register = instruction[0]
        operator = instruction[1]
        value = instruction[2]
        condition_register = instruction[3]
        condition_operator = instruction[4]
        condition_value = instruction[5]

        if condition_operator == '<':
            if registers.get(condition_register) < condition_value:
                if operator == 'inc':
                    registers.update({register: registers.get(register) + value})
                if operator == 'dec':
                    registers.update({register: registers.get(register) - value})
        if condition_operator == '>':
            if registers.get(condition_register) > condition_value:
                if operator == 'inc':
                    registers.update({register: registers.get(register) + value})
                if operator == 'dec':
                    registers.update({register: registers.get(register) - value})
        if condition_operator == '>=':
            if registers.get(condition_register) >= condition_value:
                if operator == 'inc':
                    registers.update({register: registers.get(register) + value})
                if operator == 'dec':
                    registers.update({register: registers.get(register) - value})
        if condition_operator == '<=':
            if registers.get(condition_register) <= condition_value:
                if operator == 'inc':
                    registers.update({register: registers.get(register) + value})
                if operator == 'dec':
                    registers.update({register: registers.get(register) - value})
        if condition_operator == '==':
            if registers.get(condition_register) == condition_value:
                if operator == 'inc':
                    registers.update({register: registers.get(register) + value})
                if operator == 'dec':
                    registers.update({register: registers.get(register) - value})
        if condition_operator == '!=':
            if registers.get(condition_register) != condition_value:
                if operator == 'inc':
                    registers.update({register: registers.get(register) + value})
                if operator == 'dec':
                    registers.update({register: registers.get(register) - value})

    return max(registers.values())


def main():
    test_1 = execute(test_input_1)
    answer = execute(input_data)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
