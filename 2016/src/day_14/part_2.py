from day_14.part_1 import generate_pad
from day_14.part_1 import test_input_1
from day_14.part_1 import input_data


def main():
    test_1 = generate_pad(test_input_1, show_progress=1, stretch=2017)
    answer = generate_pad(input_data, show_progress=1, stretch=2017)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
