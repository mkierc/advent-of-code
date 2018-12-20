test_input_1 = [
    [[3, 0, 0], [2, 0, 0], [-1, 0, 0]],
    [[4, 0, 0], [0, 0, 0], [-2, 0, 0]]
]


def parse_input():
    with open('data.txt') as file:
        lines = file.read().split('\n')

    input_data = []

    for line in lines:
        particle = []
        for parameter in line.split(', '):
            particle.append(list(map(int, parameter[3:-1].split(","))))
        input_data.append(particle)

    return input_data


def simulate(particles, expected_confidence):
    confidence = 0
    current_closest = 0

    while confidence < expected_confidence:
        # update the velocities and positions
        for particle in particles:
            particle[1][0] += particle[2][0]
            particle[1][1] += particle[2][1]
            particle[1][2] += particle[2][2]
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[0][2] += particle[1][2]

        # get first particle, find it's distance
        minimal_distance = 0
        for position in particles[0][0]:
            minimal_distance += abs(position)

        # check if there's any particle with lower distance
        new_closest = -1
        for particle in particles:
            current_distance = 0
            for position in particle[0]:
                current_distance += abs(position)
            if current_distance <= minimal_distance:
                minimal_distance = current_distance
                new_closest = particles.index(particle)

        # if closest particle didn't change in this step, increase the confidence
        # otherwise change the particle and reset the confidence
        if new_closest == current_closest:
            confidence += 1
        else:
            current_closest = new_closest
            confidence = 0

    return current_closest


def main():
    test_1 = simulate(test_input_1, 250)
    print("test_1:", test_1)

    answer = simulate(parse_input(), 250)
    print("answer:", answer)


if __name__ == "__main__":
    main()
