import matplotlib.pyplot as plt

data_x = [
    10000,
    20000,
    30000,
    40000,
    50000,
    60000,
    70000,
    80000,
    90000,
    100000,
    110000,
    120000,
    130000,
    140000,
    150000,
    160000,
    170000
]
data_y = [
    0.2717514,
    1.1400308,
    2.6085634,
    4.6817502,
    7.3493192,
    10.6131870,
    14.4811995,
    18.9508862,
    24.0068151,
    29.7068729,
    35.9707674,
    42.8768818,
    50.3933198,
    58.5908844,
    67.4257111,
    76.9266819,
    87.0808138
]


def y(x):
    return 3.071247227 * 10 ** (-9) * x ** 2 - 1.210640658 * 10 ** (-5) * x + 1.988593495 * 10 ** (-1)


def main():
    # define the plot size
    width = 1280
    height = 720
    ppi = 72
    plt.figure(figsize=(width / ppi, height / ppi), dpi=ppi)

    # define colors
    green = (0.12, 0.75, 0.27)
    red = (0.92, 0.30, 0.27)

    # calculate values for extrapolation function
    ex_x = [_ for _ in range(0, 203001, 1000)]
    ex_y = []

    for x in ex_x:
        ex_y.append(y(x))

    # print the plot
    plt.plot(ex_x, ex_y, 'k-', linewidth=1)
    plt.plot(data_x, data_y, linestyle='none', marker='x', color=green, markersize=10, markeredgewidth=2)
    plt.plot(200000, 121.8512763, linestyle='none', marker='x', color=red, markersize=10, markeredgewidth=2)

    plt.savefig("extrapolation_plot.png", dpi=ppi, bbox_inches="tight")


if __name__ == "__main__":
    main()
