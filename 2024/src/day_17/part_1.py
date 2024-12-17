import re
from typing import List

with open("data.txt") as file:
    regs, instructions = file.read().split('\n\n')
    a, b, c = [int(re.findall('(\d+)', reg)[0]) for reg in regs.splitlines()]
    instructions = [int(inst) for inst in instructions.split(' ')[1].split(',')]


class ChronospatialProcessor:
    def __init__(self, a: int, b: int, c: int, instruction_list: List[int]):
        self.register = {
            "a": a,
            "b": b,
            "c": c
        }
        self.pointer = 0
        self.instruction_list = instruction_list
        self.output = []

    def adv(self, x: int):
        self.register['a'] = int(self.register['a'] / pow(2, x))
        self.pointer += 2

    def bxl(self, x: int):
        self.register['b'] = self.register['b'] ^ x
        self.pointer += 2

    def bst(self, x: int):
        self.register['b'] = x % 8
        self.pointer += 2

    def jnz(self, x: int):
        if self.register['a'] == 0:
            self.pointer += 2
        else:
            self.pointer = x

    def bxc(self, x: int):
        self.register['b'] = self.register['b'] ^ self.register['c']
        self.pointer += 2

    def out(self, x: int):
        self.output.append(str(x % 8))
        self.pointer += 2

    def bdv(self, x: int):
        self.register['b'] = int(self.register['a'] / pow(2, x))
        self.pointer += 2

    def cdv(self, x: int):
        self.register['c'] = int(self.register['a'] / pow(2, x))
        self.pointer += 2

    def combo_operand(self, operand: int):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.register['a']
        elif operand == 5:
            return self.register['b']
        elif operand == 6:
            return self.register['c']
        else:
            raise NotImplementedError

    def exec(self, instruction: int, operand: int):
        if instruction == 0:
            self.adv(self.combo_operand(operand))
        elif instruction == 1:
            self.bxl(operand)
        elif instruction == 2:
            self.bst(self.combo_operand(operand))
        elif instruction == 3:
            self.jnz(operand)
        elif instruction == 4:
            self.bxc(operand)
        elif instruction == 5:
            self.out(self.combo_operand(operand))
        elif instruction == 6:
            self.bdv(self.combo_operand(operand))
        elif instruction == 7:
            self.cdv(self.combo_operand(operand))
        else:
            raise NotImplementedError

    def begin(self):
        # print(self.instruction_list)
        while self.pointer < len(self.instruction_list) - 1:
            # print(self.pointer, self.register, self.instruction_list[self.pointer], self.output)
            self.exec(self.instruction_list[self.pointer], self.instruction_list[self.pointer + 1])
        # print(self.pointer, self.register, self.output)


test_case_1 = (729, 0, 0, [0, 1, 5, 4, 3, 0])
test_case_2 = (0, 0, 9, [2, 6])
test_case_3 = (10, 0, 0, [5, 0, 5, 1, 5, 4])
test_case_4 = (2024, 0, 0, [0, 1, 5, 4, 3, 0])
test_case_5 = (0, 2024, 43690, [4, 0])


def main():
    test_processor_1 = ChronospatialProcessor(*test_case_1)
    test_processor_1.begin()
    test_1 = ','.join(test_processor_1.output)
    print("test_1:", test_1)

    test_processor_2 = ChronospatialProcessor(*test_case_2)
    test_processor_2.begin()
    test_2 = test_processor_2.register
    print("test_2:", test_2)

    test_processor_3 = ChronospatialProcessor(*test_case_3)
    test_processor_3.begin()
    test_3 = ','.join(test_processor_3.output), test_processor_3.register
    print("test_3:", test_3)

    test_processor_4 = ChronospatialProcessor(*test_case_4)
    test_processor_4.begin()
    test_4 = test_processor_4.register
    print("test_4:", test_4)

    test_processor_5 = ChronospatialProcessor(*test_case_5)
    test_processor_5.begin()
    test_5 = test_processor_5.register
    print("test_5:", test_5)

    # processor = ChronospatialProcessor(((8*8+3)*8+5)*8, b, c, instructions)  # manually searching for patterns
    processor = ChronospatialProcessor(a, b, c, instructions)
    processor.begin()
    answer = ','.join(processor.output)
    print("answer:", answer)


if __name__ == "__main__":
    main()
