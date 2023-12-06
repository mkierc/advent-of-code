test_time = [7, 15, 30]
test_distance = [9, 40, 200]

time = [41, 96, 88, 94]
distance = [214, 1789, 1127, 1055]


def simulate_races(_time, _distance):
    record_product = 1

    for i in range(len(_time)):
        race_duration =_time[i]
        record = _distance[i]

        new_records = []

        for hold_time in range(race_duration):
            time_left = race_duration - hold_time
            new_distance = time_left * hold_time
            if new_distance > record:
                new_records.append(new_distance)

        record_product *= len(new_records)

    return record_product


def main():
    test = simulate_races(test_time, test_distance)
    print("test:", test)

    answer = simulate_races(time, distance)
    print("answer:", answer)


if __name__ == "__main__":
    main()
