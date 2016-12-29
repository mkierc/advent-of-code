from day_03.part_1 import input_data
from day_03.part_1 import test_input_1
from day_03.part_1 import count_triangles


def transpose(triangle_list):
    transposed = []

    for side in range(0, len(triangle_list), 3):
        [col_a, col_b, col_c] = zip(*[triangle_list[side], triangle_list[side + 1], triangle_list[side + 2]])
        transposed.append(list(col_a))
        transposed.append(list(col_b))
        transposed.append(list(col_c))

    return transposed


def main():
    test_1 = count_triangles(transpose(test_input_1))
    answer = count_triangles(transpose(input_data))

    print("test_1:", test_1)
    print("answer:", answer)

if __name__ == "__main__":
    main()
