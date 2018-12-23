with open('data.txt') as file:
    input_data = file.read().splitlines()


# Class skeleton stolen from my Duet Processor implementation (AoC 2017 - Day 18)
class CoProcessor(object):
    def __init__(self, instruction_list):
        self.register = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0
        }
        self.pointer = 0
        self.counter = 0
        self.instruction_list = instruction_list

    def set(self, x: str, y: str):
        if y.isalpha():
            self.register[x] = self.register[y]
        else:
            self.register[x] = int(y)
        self.pointer += 1

    def sub(self, x: str, y: str):
        if y.isalpha():
            self.register[x] -= self.register[y]
        else:
            self.register[x] -= int(y)
        self.pointer += 1

    def mul(self, x: str, y: str):
        if y.isalpha():
            self.register[x] *= self.register[y]
        else:
            self.register[x] *= int(y)
        self.pointer += 1
        self.counter += 1

    def jnz(self, x: str, y: str):
        if x.isalpha():
            if y.isalpha():
                if self.register[x] != 0:
                    self.pointer += self.register[y]
                else:
                    self.pointer += 1
            else:
                if self.register[x] != 0:
                    self.pointer += int(y)
                else:
                    self.pointer += 1
        else:
            if y.isalpha():
                if int(x) != 0:
                    self.pointer += self.register[y]
                else:
                    self.pointer += 1
            else:
                if int(x) != 0:
                    self.pointer += int(y)
                else:
                    self.pointer += 1

    def exec(self):
        splitted = self.instruction_list[self.pointer].split()
        if splitted[0] == "set":
            self.set(splitted[1], splitted[2])
        elif splitted[0] == "sub":
            self.sub(splitted[1], splitted[2])
        elif splitted[0] == "mul":
            self.mul(splitted[1], splitted[2])
        elif splitted[0] == "jnz":
            self.jnz(splitted[1], splitted[2])
        else:
            raise NotImplementedError

    def begin(self):
        while self.pointer < len(self.instruction_list):
            self.exec()


def main():
    processor = CoProcessor(input_data)
    processor.begin()
    answer = processor.counter
    print("answer:", answer)


if __name__ == "__main__":
    main()
