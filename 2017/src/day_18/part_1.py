from collections import defaultdict

test_input_1 = [
    'set a 1',
    'add a 2',
    'mul a a',
    'mod a 5',
    'snd a',
    'set a 0',
    'rcv a',
    'jgz a -1',
    'set a 1',
    'jgz a -2'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


# Class skeleton stolen from my Assembunny Processor implementation (AoC 2016 - Day 12)
class DuetProcessor(object):
    def __init__(self, instruction_list):
        self.register = defaultdict(int)
        self.pointer = 0
        self.instruction_list = instruction_list

    def snd(self, x: str):
        # *the program whistles silently*
        if x.isalpha():
            self.register['last_played'] = self.register[x]
        else:
            self.register['last_played'] = int(x)
        self.pointer += 1

    def set(self, x: str, y: str):
        if y.isalpha():
            self.register[x] = self.register[y]
        else:
            self.register[x] = int(y)
        self.pointer += 1

    def add(self, x: str, y: str):
        if y.isalpha():
            self.register[x] += self.register[y]
        else:
            self.register[x] += int(y)
        self.pointer += 1

    def mul(self, x: str, y: str):
        if y.isalpha():
            self.register[x] *= self.register[y]
        else:
            self.register[x] *= int(y)
        self.pointer += 1

    def mod(self, x: str, y: str):
        if y.isalpha():
            self.register[x] %= self.register[y]
        else:
            self.register[x] %= int(y)
        self.pointer += 1

    def rcv(self, x: str):
        if x.isalpha():
            if self.register[x] != 0:
                self.pointer = len(self.instruction_list) + 1
        else:
            if int(x) != 0:
                self.pointer = len(self.instruction_list) + 1
        self.pointer += 1

    def jgz(self, x: str, y: str):
        if x.isalpha():
            if y.isalpha():
                if self.register[x] > 0:
                    self.pointer += self.register[y]
                else:
                    self.pointer += 1
            else:
                if self.register[x] > 0:
                    self.pointer += int(y)
                else:
                    self.pointer += 1
        else:
            if y.isalpha():
                if int(x) > 0:
                    self.pointer += self.register[y]
                else:
                    self.pointer += 1
            else:
                if int(x) > 0:
                    self.pointer += int(y)
                else:
                    self.pointer += 1

    def exec(self, instruction: str):
        splitted = instruction.split()
        if splitted[0] == "snd":
            self.snd(splitted[1])
        elif splitted[0] == "set":
            self.set(splitted[1], splitted[2])
        elif splitted[0] == "add":
            self.add(splitted[1], splitted[2])
        elif splitted[0] == "mul":
            self.mul(splitted[1], splitted[2])
        elif splitted[0] == "mod":
            self.mod(splitted[1], splitted[2])
        elif splitted[0] == "rcv":
            self.rcv(splitted[1])
        elif splitted[0] == "jgz":
            self.jgz(splitted[1], splitted[2])
        else:
            raise NotImplementedError

    def begin(self):
        while self.pointer < len(self.instruction_list):
            self.exec(self.instruction_list[self.pointer])


def main():
    test_processor = DuetProcessor(test_input_1)
    test_processor.begin()
    test_1 = test_processor.register['last_played']
    print("test_1:", test_1)

    processor = DuetProcessor(input_data)
    processor.begin()
    answer = processor.register['last_played']
    print("answer:", answer)


if __name__ == "__main__":
    main()
