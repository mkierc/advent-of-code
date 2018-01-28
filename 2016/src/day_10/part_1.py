with open("data.txt") as file:
    input_data = file.read().splitlines()

values = {}
factory = {}


class Output:
    def __init__(self, _id: int):
        self._id = _id
        self.value = None

    def receive(self, value: int):
        self.value = value


class Bot:
    def __init__(self, _id: int, lower_out: int, higher_out: int):
        self._id = _id
        self.lower_out = lower_out
        self.higher_out = higher_out
        self.value = None

    def receive(self, value: int):
        if self.value is None:
            self.value = value
        else:
            if self.value < value:
                lower = self.value
                higher = value
            elif self.value > value:
                lower = value
                higher = self.value
            else:
                raise NotImplementedError

            if lower == 17 and higher == 61:
                print("answer:", self._id)
            self.value = None
            factory[self.higher_out].receive(higher)
            factory[self.lower_out].receive(lower)


def parse_instruction(instruction: str):
    if instruction.startswith("value"):
        splitted = instruction.split()

        value = int(splitted[1])
        bot_id = int(splitted[5])
        values.update({
            value: bot_id
        })
    elif instruction.startswith("bot"):
        splitted = instruction.split()

        bot_id = int(splitted[1])
        receiving_type_1 = splitted[5][0]
        receiving_id_1 = int(splitted[6])
        receiving_type_2 = splitted[10][0]
        receiving_id_2 = int(splitted[11])

        # give the outputs negative id's to tell them apart from bots
        if receiving_type_1 == "o":
            receiving_id_1 = -receiving_id_1
            factory.update({receiving_id_1: Output(receiving_id_1)})
        if receiving_type_2 == "o":
            receiving_id_2 = -receiving_id_2
            factory.update({receiving_id_2: Output(receiving_id_2)})

        factory.update({bot_id: Bot(bot_id, receiving_id_1, receiving_id_2)})
    else:
        raise NotImplementedError


def main():
    for line in input_data:
        parse_instruction(line)

    for chip_value in values:
        self_id = values[chip_value]
        bot = factory.get(self_id)
        bot.receive(chip_value)


if __name__ == "__main__":
    main()
