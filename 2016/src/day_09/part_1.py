import re

test_input_1 = "ADVENT"
test_input_2 = "A(1x5)BC"
test_input_3 = "(3x3)XYZ"
test_input_4 = "A(2x2)BCD(2x2)EFG"
test_input_5 = "(6x1)(1x3)A"
test_input_6 = "X(8x2)(3x3)ABCY"

with open("data.txt") as file:
    input_data = file.read()


def decompress(compressed_data):
    decompressed_data = ""
    current_marker = 0

    while True:
        # search for next occurence of metadata marker, i.e. (12x5)
        uncompressed = compressed_data[current_marker:]
        matched = re.search(r"\((\d+)x(\d+)\)", uncompressed)

        if matched:
            # get all metadata from marker
            length = int(matched.groups()[0])
            multiplier = int(matched.groups()[1])
            marker_start = current_marker + matched.start()
            marker_end = current_marker + matched.end()

            # append data upto where marker is
            decompressed_data += compressed_data[current_marker:marker_start]

            # decompress data using marker metadata
            for i in range(multiplier):
                decompressed_data += compressed_data[marker_end:marker_end + length]

            # move current datapoint marker to point after decompressed data
            current_marker = marker_end + length
        else:
            # append the rest of data after last marker data was decompressed
            decompressed_data += compressed_data[current_marker:]
            break

    return decompressed_data


def main():
    test_1 = len(decompress(test_input_1))
    print("test_1:", test_1)
    test_2 = len(decompress(test_input_2))
    print("test_2:", test_2)
    test_3 = len(decompress(test_input_3))
    print("test_3:", test_3)
    test_4 = len(decompress(test_input_4))
    print("test_4:", test_4)
    test_5 = len(decompress(test_input_5))
    print("test_3:", test_5)
    test_6 = len(decompress(test_input_6))
    print("test_4:", test_6)

    answer = len(decompress(input_data))
    print("answer:", answer)


if __name__ == "__main__":
    main()
