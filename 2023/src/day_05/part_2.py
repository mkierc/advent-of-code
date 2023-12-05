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
    seed_ranges = [[int(y) for y in x] for x in re.findall(r' (\d+) (\d+)', _map[0])]
    seed_to_soil = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[1])]
    soil_to_fert = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[2])]
    fert_to_watr = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[3])]
    watr_to_lght = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[4])]
    lght_to_temp = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[5])]
    temp_to_humd = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[6])]
    humd_to_lctn = [[int(y) for y in x] for x in re.findall(r'(\d+) (\d+) (\d+)', _map[7])]

    return seed_ranges, seed_to_soil, soil_to_fert, fert_to_watr, watr_to_lght, lght_to_temp, temp_to_humd, humd_to_lctn


def find_reverse_mapping(_lctn, _map):
    for start_to, start_from, map_range in _map:
        if start_to <= _lctn < start_to + map_range:
            return start_from + (_lctn - start_to)
    return _lctn


def validate_seed(_almanac):
    seed_ranges, seed_to_soil, soil_to_fert, fert_to_watr, watr_to_lght, lght_to_temp, temp_to_humd, humd_to_lctn = parse_map(
        _almanac)

    lctn = 0

    while True:
        # debug counter, to see viability of solution speed:
        # if lctn % 100_000 == 0:
        #     print(lctn)
        humd = find_reverse_mapping(lctn, humd_to_lctn)
        temp = find_reverse_mapping(humd, temp_to_humd)
        lght = find_reverse_mapping(temp, lght_to_temp)
        watr = find_reverse_mapping(lght, watr_to_lght)
        fert = find_reverse_mapping(watr, fert_to_watr)
        soil = find_reverse_mapping(fert, soil_to_fert)
        seed = find_reverse_mapping(soil, seed_to_soil)

        for _seed_start, _range in seed_ranges:
            if _seed_start <= seed < _seed_start + _range:
                return seed, lctn
        lctn += 1


def main():
    test = validate_seed(test_input)
    print("test:", test)

    answer = validate_seed(almanac)
    print("answer:", answer)


if __name__ == "__main__":
    main()
