import re

test_input_1 = [
    ['London', 'Dublin', 464],
    ['London', 'Belfast', 518],
    ['Dublin', 'Belfast', 141]
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


def parse(raw_connection_list):
    connection_list = []

    for line in raw_connection_list:
        city_from, city_to, distance = re.search(r'([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)', line).groups()
        connection_list.append([city_from, city_to, int(distance)])

    return connection_list


def find_routes(current_routes, available_destinations):
    routes = []

    for destination in available_destinations:
        new_available_destinations = available_destinations[:]
        new_routes = current_routes[:]

        new_routes.append(destination)
        new_available_destinations.remove(destination)

        if not new_available_destinations:
            routes.append(new_routes + new_available_destinations)

        routes.extend(find_routes(new_routes, new_available_destinations))

    return routes


def calculate_route_distance(route, connection_list):
    distance = 0

    for city_1, city_2 in zip(route, route[1:]):
        for connection in connection_list:
            if (city_1 == connection[0] and city_2 == connection[1]) \
                    or (city_1 == connection[1] and city_2 == connection[0]):
                distance += connection[2]

    return distance


def calculate_shortest_and_longest_distance(connection_list):
    cities = set()

    for connection in connection_list:
        cities.add(connection[0])
        cities.add(connection[1])

    routes = find_routes([], list(cities))

    shortest_distance = calculate_route_distance(routes[0], connection_list)
    longest_distance = calculate_route_distance(routes[0], connection_list)

    for route in routes[1:]:
        new_distance = calculate_route_distance(route, connection_list)
        if new_distance < shortest_distance:
            shortest_distance = new_distance
        if new_distance > longest_distance:
            longest_distance = new_distance

    return shortest_distance, longest_distance


def main():
    test_1 = calculate_shortest_and_longest_distance(test_input_1)
    print('test_1:', test_1[0])
    print('test_2:', test_1[1])

    answer = calculate_shortest_and_longest_distance(parse(input_data))
    print('part_1:', answer[0])
    print('part_2:', answer[1])


if __name__ == '__main__':
    main()
