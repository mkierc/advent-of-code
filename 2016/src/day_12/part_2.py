from day_12.part_1 import AssembunnyProcessor
from day_12.part_1 import input_data


def main():
    processor = AssembunnyProcessor(input_data)
    processor.register.update({"c": 1})
    processor.begin()
    answer = processor.register["a"]

    print("answer:", answer)


if __name__ == "__main__":
    main()
