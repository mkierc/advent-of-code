import copy

weapons = [
    {'name': 'Dagger', 'cost': 8, 'damage': 4, 'armor': 0},
    {'name': 'Shortsword', 'cost': 10, 'damage': 5, 'armor': 0},
    {'name': 'Warhammer', 'cost': 25, 'damage': 6, 'armor': 0},
    {'name': 'Longsword', 'cost': 40, 'damage': 7, 'armor': 0},
    {'name': 'Greataxe', 'cost': 74, 'damage': 8, 'armor': 0}
]

armors = [
    {'name': 'empty_slot', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'Leather', 'cost': 13, 'damage': 0, 'armor': 1},
    {'name': 'Chainmail', 'cost': 31, 'damage': 0, 'armor': 2},
    {'name': 'Splintmail', 'cost': 53, 'damage': 0, 'armor': 3},
    {'name': 'Bandedmail', 'cost': 75, 'damage': 0, 'armor': 4},
    {'name': 'Platemail', 'cost': 102, 'damage': 0, 'armor': 5}
]

rings = [
    {'name': 'empty_slot_1', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'empty_slot_2', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'Damage +1', 'cost': 25, 'damage': 1, 'armor': 0},
    {'name': 'Damage +2', 'cost': 50, 'damage': 2, 'armor': 0},
    {'name': 'Damage +3', 'cost': 100, 'damage': 3, 'armor': 0},
    {'name': 'Defense +1', 'cost': 20, 'damage': 0, 'armor': 1},
    {'name': 'Defense +2', 'cost': 40, 'damage': 0, 'armor': 2},
    {'name': 'Defense +3', 'cost': 80, 'damage': 0, 'armor': 3}
]

test_boss_stats = {
    'hp': 12,
    'damage': 7,
    'armor': 2
}
test_player_stats = {
    'hp': 8,
    'damage': 5,
    'armor': 5
}

input_boss_stats = {
    'hp': 103,
    'damage': 9,
    'armor': 2
}
input_player_stats = {
    'hp': 100,
    'damage': 0,
    'armor': 0
}


def simulate_fight(boss_stats, player_stats, item_list):
    boss_stats = copy.copy(boss_stats)
    player_stats = copy.copy(player_stats)

    # use player items
    for item in item_list:
        player_stats['damage'] += item['damage']
        player_stats['armor'] += item['armor']

    # simulate the fight until someone dies
    while True:
        # player attacks first
        # calculate damage
        player_attack = player_stats['damage'] - boss_stats['armor']
        # at least one hp of damage must be dealt
        if player_attack < 1:
            player_attack = 1
        # deal the damage
        boss_stats['hp'] -= player_attack
        # check if boss is still alive
        if boss_stats['hp'] <= 0:
            break

        # boss attacks second
        # calculate damage
        boss_attack = boss_stats['damage'] - player_stats['armor']
        # at least one hp of damage must be dealt
        if boss_attack < 1:
            boss_attack = 1
        # deal the damage
        player_stats['hp'] -= boss_attack
        # check if boss is still alive
        if player_stats['hp'] <= 0:
            break

    return {
        'boss_hp': boss_stats['hp'],
        'player_hp': player_stats['hp']
    }


def generate_itemsets():
    # generate all the legal item sets
    item_sets = []
    for weapon in weapons:
        for armor in armors:
            for ring_1 in rings:
                for ring_2 in rings[:rings.index(ring_1)] + rings[rings.index(ring_1) + 1:]:
                    items = [weapon, armor, ring_1, ring_2]
                    cost = sum(x['cost'] for x in items)
                    item_sets.append({'cost': cost, 'items': items})
    return item_sets


def find_cheapest_win(item_sets):
    # sort items by cost, find first one that makes the player win
    for item_set in sorted(item_sets, key=lambda x: x['cost']):
        fight_result = simulate_fight(input_boss_stats, input_player_stats, item_set['items'])['player_hp']
        if fight_result > 0:
            return item_set['cost']


def find_most_expensive_loss(item_sets):
    # sort items by cost (in descending order), find first one that makes the player lose
    for item_set in sorted(item_sets, key=lambda x: x['cost'], reverse=True):
        fight_result = simulate_fight(input_boss_stats, input_player_stats, item_set['items'])['boss_hp']
        if fight_result > 0:
            return item_set['cost']


def main():
    test_1 = simulate_fight(test_boss_stats, test_player_stats, [])
    print('test_1:', test_1)

    answer = find_cheapest_win(generate_itemsets())
    print('part_1:', answer)
    answer = find_most_expensive_loss(generate_itemsets())
    print('part_2:', answer)


if __name__ == '__main__':
    main()
