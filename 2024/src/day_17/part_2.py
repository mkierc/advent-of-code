import re
from time import time
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

    def begin(self):
        while self.pointer < len(self.instruction_list) - 1:
            self.exec(self.instruction_list[self.pointer], self.instruction_list[self.pointer + 1])

    def step(self):
        self.exec(self.instruction_list[self.pointer], self.instruction_list[self.pointer + 1])

    # # this pruning function is not efficient enough for actual input
    #
    # def compare_output(self, instruction_list):
    #     for i, char in enumerate(self.output):
    #         if int(char) != instruction_list[i]:
    #             return False
    #     return True

    def compare_output_from_back(self, instruction_list):
        for i in range(-1, -len(self.output)-1, -1):
            if int(self.output[i]) != instruction_list[i]:
                return False
        return True

    def find_register(self):
        # copy initial parameters for subsequent executions, but we don't care about register as it changes anyway
        a = 0
        b = self.register['b']
        c = self.register['c']
        instruction_list = self.instruction_list

        while True:
            # reinitialize processor, and run instructions
            self.__init__(a, b, c, instruction_list)
            while self.pointer < len(self.instruction_list) - 1:
                self.exec(self.instruction_list[self.pointer], self.instruction_list[self.pointer + 1])
                # # this will not help, while searching from the back
                # if not self.compare_output(instruction_list):
                #     break

            if self.compare_output_from_back(self.instruction_list):
                # # from the front
                # print(f'{a:>14}, {bin(a):32}', len(self.output), self.output)
                # from the back
                print(f'{a:>16} {bin(a):48} {",".join(self.output):>32} {len(self.output):>4}')

                # if entire output == instruction list, we're done
                if [int(x) for x in self.output] == instruction_list:
                    return a
                # otherwise only a subset of last digits is ok, then we skip by << 3
                else:
                    a *= 8
            a += 1

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


test_case_1 = (2024, 0, 0, [0, 3, 5, 4, 3, 0])


def main():
    test_processor_1 = ChronospatialProcessor(*test_case_1)
    test_1 = test_processor_1.find_register()
    print("test_1:", test_1)

    start = time()
    processor = ChronospatialProcessor(a, b, c, instructions)
    answer = processor.find_register()
    print("answer:", answer)
    print('time:', time() - start)


if __name__ == "__main__":
    main()

# answer:       37222273957364
# time:         0.00498652458190918 s

########################################################################################################################
# can't see any sensible patterns from the front...
########################################################################################################################
# correct up to len(3)
#          14836,                 0b11100111110100 4 ['2', '4', '1', '5']
#          15860,                 0b11110111110100 4 ['2', '4', '1', '6']
#          17165,                0b100001100001101 4 ['2', '4', '1', '4']
#          17189,                0b100001100100101 4 ['2', '4', '1', '4']
#          17197,                0b100001100101101 4 ['2', '4', '1', '4']
#          18189,                0b100011100001101 4 ['2', '4', '1', '3']
#          19213,                0b100101100001101 4 ['2', '4', '1', '4']
#          20237,                0b100111100001101 4 ['2', '4', '1', '7']
#          31220,                0b111100111110100 4 ['2', '4', '1', '5']
#          32244,                0b111110111110100 4 ['2', '4', '1', '4']
#                                  ............10.
# correct up to len(4)
#          41829,               0b1010001101100101 5 ['2', '4', '1', '2', '1']
#          41837,               0b1010001101101101 5 ['2', '4', '1', '2', '1']
#         107365,              0b11010001101100101 5 ['2', '4', '1', '2', '1']
#         107373,              0b11010001101101101 5 ['2', '4', '1', '2', '1']
#         172901,             0b101010001101100101 5 ['2', '4', '1', '2', '1']
#         172909,             0b101010001101101101 5 ['2', '4', '1', '2', '1']
#         238437,             0b111010001101100101 5 ['2', '4', '1', '2', '1']
#         238445,             0b111010001101101101 5 ['2', '4', '1', '2', '1']
#                               ..10100011011..101
# correct up to len(5)
#          48628,               0b1011110111110100 6 ['2', '4', '1', '2', '7', '0']
#         114164,              0b11011110111110100 6 ['2', '4', '1', '2', '7', '3']
#         179700,             0b101011110111110100 6 ['2', '4', '1', '2', '7', '4']
#         244212,             0b111011100111110100 6 ['2', '4', '1', '2', '7', '6']
#         245236,             0b111011110111110100 6 ['2', '4', '1', '2', '7', '6']
#         260596,             0b111111100111110100 6 ['2', '4', '1', '2', '7', '6']
#         310772,            0b1001011110111110100 6 ['2', '4', '1', '2', '7', '1']
#         376308,            0b1011011110111110100 6 ['2', '4', '1', '2', '7', '7']
#         441844,            0b1101011110111110100 6 ['2', '4', '1', '2', '7', '4']
#         506356,            0b1111011100111110100 6 ['2', '4', '1', '2', '7', '6']
#         507380,            0b1111011110111110100 6 ['2', '4', '1', '2', '7', '6']
#         572916,           0b10001011110111110100 6 ['2', '4', '1', '2', '7', '2']
#         638452,           0b10011011110111110100 6 ['2', '4', '1', '2', '7', '3']
#                                 1.11..0111110100

########################################################################################################################
# checking from the back, the numbers seem to follow a pattern, each one of the next levels are at least 8 times greater
########################################################################################################################
#
#                1 0b1                                                                             0    1
#                8 0b1000                                                                        3,0    2
#               67 0b1000011                                                                   3,3,0    3
#               70 0b1000110                                                                   3,3,0    3
#              541 0b1000011101                                                              0,3,3,0    4
#              565 0b1000110101                                                              0,3,3,0    4
#             4329 0b1000011101001                                                         5,0,3,3,0    5
#             4333 0b1000011101101                                                         5,0,3,3,0    5
#             4521 0b1000110101001                                                         5,0,3,3,0    5
#             4526 0b1000110101110                                                         5,0,3,3,0    5
#            34665 0b1000011101101001                                                    5,5,0,3,3,0    6
#            34671 0b1000011101101111                                                    5,5,0,3,3,0    6
#            36208 0b1000110101110000                                                    5,5,0,3,3,0    6
#            36215 0b1000110101110111                                                    5,5,0,3,3,0    6
#           277327 0b1000011101101001111                                               4,5,5,0,3,3,0    7
#           289726 0b1000110101110111110                                               4,5,5,0,3,3,0    7
