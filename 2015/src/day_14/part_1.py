import re

test_input_1 = [
    'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
    'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
]

reindeer_regex = re.compile(r'([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

with open('data.txt') as file:
    input_data = file.read().splitlines()


class Reindeer(object):
    def __init__(self, name, speed, flying_time, resting_time):
        self.name = name
        self.speed = speed
        self.flying_time = flying_time
        self.resting_time = resting_time
        self.state = 'flying'
        self.distance = 0
        self.time_in_current_state = 0

    def __invert__(self):
        # check state, update distance
        if self.state == 'flying':
            self.distance += self.speed
            self.time_in_current_state += 1
        elif self.state == 'resting':
            self.time_in_current_state += 1

        # check if we should update state
        if self.state == 'flying' and self.time_in_current_state == self.flying_time:
            self.state = 'resting'
            self.time_in_current_state = 0
        elif self.state == 'resting' and self.time_in_current_state == self.resting_time:
            self.state = 'flying'
            self.time_in_current_state = 0


def parse(raw_data):
    reindeers = []

    for line in raw_data:
        name, speed, flying_time, resting_time = re.match(reindeer_regex, line).groups()
        reindeers.append(Reindeer(name, int(speed), int(flying_time), int(resting_time)))

    return reindeers


def solve(raw_data, tick_count):
    reindeers = parse(raw_data)

    for tick in range(tick_count):
        for reindeer in reindeers:
            ~reindeer

    return max([x.distance for x in reindeers])


def main():
    test_1 = solve(test_input_1, 1000)
    print('test_1:', test_1)

    answer = solve(input_data, 2503)
    print('answer:', answer)


if __name__ == '__main__':
    main()
