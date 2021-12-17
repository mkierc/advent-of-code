test_area = (20, 30, -10, -5)
input_area = (143, 177, -106, -71)


def calculate_velocity(_area):
    min_x, max_x, min_y, max_y = _area

    trajectories = []
    for d_0 in range(0, 500):
        d_y = d_0
        y_max = 0
        y = 0
        while y >= min_y:
            y += d_y
            d_y -= 1
            if y > y_max:
                y_max = y
            if min_y <= y <= max_y:
                trajectories.append([y_max, d_0])
    return sorted(trajectories, key=lambda x: x[0], reverse=True)[0][0]


def main():
    test = calculate_velocity(test_area)
    print(f"test: {test}")

    answer = calculate_velocity(input_area)
    print(f"answer: {answer}")


if __name__ == "__main__":
    main()
