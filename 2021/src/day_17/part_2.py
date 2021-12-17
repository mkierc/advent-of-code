import time

test_area = (20, 30, -10, -5)
input_area = (143, 177, -106, -71)


def calculate_velocity(_area):
    min_x, max_x, min_y, max_y = _area

    trajectories = set()
    for d_x_0 in range(0, 500):
        start = time.time()
        for d_y_0 in range(-200, 500):
            d_y = d_y_0
            d_x = d_x_0
            y = 0
            x = 0
            while y >= min_y and x <= max_x:
                y += d_y
                d_y -= 1
                x += d_x
                if d_x > 0:
                    d_x -= 1
                if min_y <= y <= max_y and min_x <= x <= max_x:
                    trajectories.add((d_x_0, d_y_0))
        if d_x_0 % 50 == 0:
            print(f'{d_x_0} to {d_x_0 + 50} in {time.time() - start:.10f}s found {len(trajectories)} trajectories')
    return len(trajectories)


def main():
    test = calculate_velocity(test_area)
    print(f"test: {test}")

    answer = calculate_velocity(input_area)
    print(f"answer: {answer}")


if __name__ == "__main__":
    main()
