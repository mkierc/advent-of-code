import itertools

test_input_1 = [
    [[-6, 0, 0], [3, 0, 0], [0, 0, 0]],
    [[-4, 0, 0], [2, 0, 0], [0, 0, 0]],
    [[-2, 0, 0], [1, 0, 0], [0, 0, 0]],
    [[3, 0, 0], [-1, 0, 0], [0, 0, 0]]
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
    current_count = 0

    while confidence < expected_confidence:
        # update the velocities and positions
        for particle in particles:
            particle[1][0] += particle[2][0]
            particle[1][1] += particle[2][1]
            particle[1][2] += particle[2][2]
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[0][2] += particle[1][2]

        # mark collided particles for deletion
        to_delete = []
        for particle_1, particle_2 in itertools.combinations(particles, 2):
            if particle_1[0] == particle_2[0]:
                to_delete.append(particle_1)
                to_delete.append(particle_2)

        # delete particles that collided
        for particle in to_delete:
            try:
                particles.remove(particle)
            except ValueError:
                pass

        # count the particles
        new_count = len(particles)

        # if particle count didn't change in this step, increase the confidence
        # otherwise change the particle count and reset the confidence
        if new_count == current_count:
            confidence += 1
        else:
            current_count = new_count
            confidence = 0

    return current_count


def main():
    test_1 = simulate(test_input_1, 10)
    print("test_1:", test_1)

    answer = simulate(parse_input(), 10)
    print("answer:", answer)


if __name__ == "__main__":
    main()
