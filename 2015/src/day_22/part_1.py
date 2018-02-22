import copy

spells = {
    'Magic Missile': {'name': 'Magic Missile', 'cost': 53, 'damage': 4, 'heal': 0, 'time': -1, 'mana': 0, 'armor': 0},
    'Drain': {'name': 'Drain', 'cost': 73, 'damage': 2, 'heal': 2, 'time': -1, 'mana': 0, 'armor': 0},
    'Shield': {'name': 'Shield', 'cost': 113, 'damage': 0, 'heal': 0, 'time': 6, 'mana': 0, 'armor': 7},
    'Poison': {'name': 'Poison', 'cost': 173, 'damage': 3, 'heal': 0, 'time': 6, 'mana': 0, 'armor': 0},
    'Recharge': {'name': 'Recharge', 'cost': 229, 'damage': 0, 'heal': 0, 'time': 5, 'mana': 101, 'armor': 0}
}

test_player_stats_1 = {
    'hp': 10,
    'armor': 0,
    'mana': 250,
    'total_mana_spend': 0
}
test_boss_stats_1 = {
    'hp': 13,
    'damage': 8
}
test_player_stats_2 = {
    'hp': 10,
    'armor': 0,
    'mana': 250,
    'total_mana_spend': 0
}
test_boss_stats_2 = {
    'hp': 14,
    'damage': 8
}

input_player_stats = {
    'hp': 50,
    'armor': 0,
    'mana': 500,
    'total_mana_spend': 0
}
input_boss_stats = {
    'hp': 51,
    'damage': 9
}


def test_fight_1(player_stats, boss_stats):
    effects = []
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Poison'])
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Magic Missile'])


def test_fight_2(player_stats, boss_stats):
    effects = []
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Recharge'])
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Shield'])
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Drain'])
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Poison'])
    player_stats, boss_stats, effects = simulate_round(player_stats, boss_stats, effects, spells['Magic Missile'])


def simulate_fight(player_stats, boss_stats):
    player_stats = copy.deepcopy(player_stats)
    boss_stats = copy.deepcopy(boss_stats)

    least_mana_spend = 999_999
    current_states = [(boss_stats, player_stats, [])]

    # if there are any states left to consider
    while current_states:
        for state in current_states:
            # generate possible new spells for all the states
            for spell in spells:
                pass

        # TODO: implement the rest of the simulation
        # simulate rounds with those spells

        # if player died, do nothing (it's kind of sad...)

        # if player won, save his total mana spend

        # if the game is still on, add the resulting state to the new list of current states

        # replace the current states list with the new list

    return least_mana_spend


# simulate one round of fight
def simulate_round(player_stats, boss_stats, active_effects: list, chosen_spell):

    # clone the states, so we don't destroy the original objects
    player_stats = copy.deepcopy(player_stats)
    boss_stats = copy.deepcopy(boss_stats)
    active_effects = copy.deepcopy(active_effects)
    chosen_spell = copy.deepcopy(chosen_spell)

    ####################################################################################################################
    # PLAYER TURN

    # print('-- Player turn --')
    # print('- Player has ' + str(player_stats['hp']) + ' hp, ' + str(player_stats['armor']) + ' armor, ' + str(player_stats['mana']) + ' mana')
    # print('- Boss has ' + str(boss_stats['hp']) + ' hp')

    # apply active effects
    for effect in active_effects:
        boss_stats['hp'] -= effect['damage']
        player_stats['hp'] += effect['heal']
        player_stats['mana'] += effect['mana']
        effect['time'] -= 1
        # print(effect['name'] + ' causes ' + str(effect['damage']) + ' dmg, ' + str(effect['heal']) + ' healing, ' + str(effect['mana']) + ' mana boost, the timer is now ' + str(effect['time']))

    # destroy effects that ended
    for effect in active_effects:
        if effect['time'] == 0:
            player_stats['armor'] -= effect['armor']
            active_effects.remove(effect)
            # print(effect['name'] + ' weared off.')

    # print('Player casts ' + chosen_spell['name'] + ', causing ' + str(chosen_spell['damage']) + ' dmg, ' + str(chosen_spell['heal']) + ' healing, ' + str(chosen_spell['armor']) + ' armor boost')

    # can we cast the spell?
    if player_stats['mana'] < chosen_spell['cost']:
        # print('Player has no mana, so he DIES')
        player_stats['hp'] = 0
        return player_stats, boss_stats, active_effects

    # use the chosen spell:
    # pull the mana from the player
    player_stats['mana'] -= chosen_spell['cost']
    player_stats['total_mana_spend'] += chosen_spell['cost']

    # use instant spells
    if chosen_spell['time'] == -1:
        boss_stats['hp'] -= chosen_spell['damage']
        player_stats['hp'] += chosen_spell['heal']
    # apply effects
    else:
        active_effects.append(chosen_spell)
        player_stats['armor'] += chosen_spell['armor']

    # check if boss is still alive
    if boss_stats['hp'] <= 0:
        # print('The boss DIED.')
        return player_stats, boss_stats, active_effects

    # print()

    ####################################################################################################################
    # BOSS TURN

    # print('-- Boss turn --')
    # print('- Player has ' + str(player_stats['hp']) + ' hp, ' + str(player_stats['armor']) + ' armor, ' + str(player_stats['mana']) + ' mana')
    # print('- Boss has ' + str(boss_stats['hp']) + ' hp')

    # apply active effects
    for effect in active_effects:
        boss_stats['hp'] -= effect['damage']
        player_stats['hp'] += effect['heal']
        player_stats['mana'] += effect['mana']
        effect['time'] -= 1
        # print(effect['name'] + ' causes ' + str(effect['damage']) + ' dmg, ' + str(effect['heal']) + ' healing, ' + str(effect['mana']) + ' mana boost, the timer is now ' + str(effect['time']))

    # destroy effects that ended
    for effect in active_effects:
        if effect['time'] == 0:
            player_stats['armor'] -= effect['armor']
            active_effects.remove(effect)
            # print(effect['name'] + ' weared off.')

    # check if boss is still alive
    if boss_stats['hp'] <= 0:
        # print('The boss DIED.')
        return player_stats, boss_stats, active_effects

    # boss attacks second
    # calculate damage
    boss_attack = boss_stats['damage'] - player_stats['armor']
    # at least one hp of damage must be dealt
    if boss_attack < 1:
        boss_attack = 1
    # deal the damage
    player_stats['hp'] -= boss_attack

    # print('Boss attacks for ' + str(boss_stats['damage']) + ' - ' + str(player_stats['armor']) + ' = ' + str(boss_attack))

    # check if player is still alive
    if player_stats['hp'] <= 0:
        # print('The player DIED.')
        return player_stats, boss_stats, active_effects

    # print()

    return player_stats, boss_stats, active_effects


def main():
    test_1 = test_fight_1(test_player_stats_1, test_boss_stats_1)
    print('test_1:', test_1)
    test_2 = test_fight_2(test_player_stats_2, test_boss_stats_2)
    print('test_2:', test_2)

    answer = simulate_fight(input_player_stats, input_boss_stats)
    print('part_1:', answer)


if __name__ == '__main__':
    main()
