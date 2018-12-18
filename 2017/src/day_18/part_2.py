from collections import defaultdict

test_input_1 = [
    'snd 1',
    'snd 2',
    'snd p',
    'rcv a',
    'rcv b',
    'rcv c',
    'rcv d'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


# Class skeleton stolen from my Assembunny Processor implementation (AoC 2016 - Day 12)
class DuetProcessor(object):
    def __init__(self, instruction_list, pid: int):
        self.register = defaultdict(int)
        self.register['p'] = pid
        self.pointer = 0
        self.counter = 0
        self.instruction_list = instruction_list
        self.sent = []
        self.partner = None
        self.halt = False

    def snd(self, x: str):
        # *the program whistles silently*
        if x.isalpha():
            self.sent.append(self.register[x])
        else:
            self.sent.append(int(x))
        self.pointer += 1
        self.counter += 1

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
        try:
            self.register[x] = self.partner.sent[0]
            del(self.partner.sent[0])
            self.pointer += 1
        except IndexError:
            self.halt = True

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

    def exec(self):
        if self.halt:
            return

        splitted = self.instruction_list[self.pointer].split()
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


def solve(instruction_set):
    processor_0 = DuetProcessor(instruction_set, 0)
    processor_1 = DuetProcessor(instruction_set, 1)
    processor_0.partner = processor_1
    processor_1.partner = processor_0

    while not processor_0.halt or not processor_1.halt:
        processor_0.exec()
        processor_1.exec()

        # If a processor have sent a message, unhalt the other one
        if processor_1.sent:
            processor_0.halt = False
        if processor_0.sent:
            processor_1.halt = False

    return processor_1.counter


def main():
    test_1 = solve(test_input_1)
    print("test_1:", test_1)

    answer = solve(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
