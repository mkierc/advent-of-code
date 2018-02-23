from collections import defaultdict

test_input_1 = [
    'inc a',
    'jio a, +2',
    'tpl a',
    'inc a'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


class MarieJaneProcessor(object):
    def __init__(self, instruction_list):
        self.register = defaultdict(lambda: 0)
        self.pointer = 0
        self.instruction_list = instruction_list

    def hlf(self, r: str):
        self.register[r] //= 2
        self.pointer += 1

    def tpl(self, r: str):
        self.register[r] *= 3
        self.pointer += 1

    def inc(self, r: str):
        self.register[r] += 1
        self.pointer += 1

    def jmp(self, offset: str):
        self.pointer += int(offset)

    def jie(self, r: str, offset: str):
        if self.register[r] % 2 == 0:
            self.pointer += int(offset)
        else:
            self.pointer += 1

    def jio(self, r: str, offset: str):
        if self.register[r] == 1:
            self.pointer += int(offset)
        else:
            self.pointer += 1

    def exec(self, instruction: str):
        splitted = instruction.replace(',', '').split()
        if splitted[0] == "hlf":
            self.hlf(splitted[1])
        elif splitted[0] == "tpl":
            self.tpl(splitted[1])
        elif splitted[0] == "inc":
            self.inc(splitted[1])
        elif splitted[0] == "jmp":
            self.jmp(splitted[1])
        elif splitted[0] == "jie":
            self.jie(splitted[1], splitted[2])
        elif splitted[0] == "jio":
            self.jio(splitted[1], splitted[2])
        else:
            raise NotImplementedError

    def begin(self):
        while self.pointer < len(self.instruction_list):
            self.exec(self.instruction_list[self.pointer])


def main():
    test_processor = MarieJaneProcessor(test_input_1)
    test_processor.begin()
    test_1 = test_processor.register['a']
    print("test_1:", test_1)

    processor_1 = MarieJaneProcessor(input_data)
    processor_1.begin()
    part_1 = processor_1.register['b']
    print("part_1:", part_1)

    processor_2 = MarieJaneProcessor(input_data)
    processor_2.register['a'] = 1
    processor_2.begin()
    part_2 = processor_2.register['b']
    print("part_2:", part_2)


if __name__ == "__main__":
    main()
