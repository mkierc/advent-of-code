import re

test_input_1 = "(3x3)XYZ"
test_input_2 = "X(8x2)(3x3)ABCY"
test_input_3 = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
test_input_4 = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

with open("data.txt") as file:
    input_data = file.read()


def get_decompressed_length(compressed_data):
    matched = re.search(r"\((\d+)x(\d+)\)", compressed_data)

    if matched:
        # get all metadata from marker
        length = int(matched.groups()[0])
        multiplier = int(matched.groups()[1])
        marker_start = matched.start()
        marker_end = matched.end()

        # get uncompressed parts
        inside = compressed_data[marker_end:marker_end + length]
        outside = compressed_data[marker_end + length:]

        # return the size of the data, with uncompressed parts computed recursively
        start = marker_start
        middle = get_decompressed_length(inside) * multiplier
        end = get_decompressed_length(outside)

        return start + middle + end
    else:
        return len(compressed_data)


def main():
    test_1 = get_decompressed_length(test_input_1)
    print("test_1:", test_1)
    test_2 = get_decompressed_length(test_input_2)
    print("test_2:", test_2)
    test_3 = get_decompressed_length(test_input_3)
    print("test_3:", test_3)
    test_4 = get_decompressed_length(test_input_4)
    print("test_4:", test_4)

    answer = get_decompressed_length(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
