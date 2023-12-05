import re

test_input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

almanac = ''

with open("data.txt") as file:
    for _line in file.readlines():
        almanac += _line


def parse_map(_map):
    _map = _map.split('\n\n')
    seed_list = [int(x) for x in re.findall(r'\d+', _map[0])]
    seed_to_soil = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[1])]
    soil_to_fert = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[2])]
    fert_to_watr = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[3])]
    watr_to_lght = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[4])]
    lght_to_temp = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[5])]
    temp_to_humd = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[6])]
    humd_to_lctn = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[7])]

    return seed_list, seed_to_soil, soil_to_fert, fert_to_watr, watr_to_lght, lght_to_temp, temp_to_humd, humd_to_lctn


def find_mapping(_seed, _map):
    for start_to, start_from, map_range in _map:
        if start_from <= _seed < start_from + map_range:
            offset = _seed - start_from
            return start_to + offset
    return _seed


def find_location(_almanac):
    seed_list, seed_to_soil, soil_to_fert, fert_to_watr, watr_to_lght, lght_to_temp, temp_to_humd, humd_to_lctn = parse_map(
        _almanac)

    lctn_list = []

    for seed in seed_list:
        soil = find_mapping(seed, seed_to_soil)
        fert = find_mapping(soil, soil_to_fert)
        watr = find_mapping(fert, fert_to_watr)
        lght = find_mapping(watr, watr_to_lght)
        temp = find_mapping(lght, lght_to_temp)
        humd = find_mapping(temp, temp_to_humd)
        lctn = find_mapping(humd, humd_to_lctn)

        lctn_list.append(lctn)

    return min(lctn_list)


def main():
    test = find_location(test_input)
    print("test:", test)

    answer = find_location(almanac)
    print("answer:", answer)


if __name__ == "__main__":
    main()
