# 0 = generator
# 1 = microchip
# 0-4 = type
import copy

actual_initial_state = [
    {(0, 0), (1, 0)},
    {(0, 1), (0, 2), (0, 3), (0, 4)},
    {(1, 1), (1, 2), (1, 3), (1, 4)},
    set(),
    0
]
initial_test_state = [
    {(1, 1), (1, 0)},
    {(0, 0)},
    {(0, 1)},
    set(),
    0
]

visited_states = [
    [initial_test_state]
]


def is_solved(state):
    return state[0] == set() and state[1] == set() and state[2] == set()


def is_floor_valid(floor):
    for item in floor:
        if item[0] == 1:  # is a microchip
            any_generator = False
            matching_generator = False
            for another_item in floor:
                if another_item[0] == 0:  # is a generator
                    any_generator = True
                    if item[1] == another_item[1]:  # are items of same type
                        matching_generator = True
                        break
            if not matching_generator and any_generator:
                return False
    return True


def is_state_valid(state):
    for floor in state[:3]:
        if not is_floor_valid(floor):
            return False
    return True


def find_possible_next_states(current_state):
    new_states = []
    # try moving things down
    if current_state[4] != 0:  # lowest floor
        # move 1 thing down
        for thing in current_state[current_state[4]]:
            new_state = copy.deepcopy(current_state)
            new_state[new_state[4]].remove(thing)
            new_state[new_state[4]-1].add(thing)
            new_state[4] -= 1
            if is_state_valid(new_state) and new_state not in new_states:
                new_states.append(new_state)
        # move 2 things down
        for thing in current_state[current_state[4]]:
            for another_thing in current_state[current_state[4]]:
                if thing != another_thing:
                    new_state = copy.deepcopy(current_state)
                    new_state[new_state[4]].remove(thing)
                    new_state[new_state[4]].remove(another_thing)
                    new_state[new_state[4]-1].add(thing)
                    new_state[new_state[4]-1].add(another_thing)
                    new_state[4] -= 1
                    if is_state_valid(new_state) and new_state not in new_states:
                        new_states.append(new_state)
    # try moving things up
    if current_state[4] != 3:  # highest floor
        # move 1 thing up
        for thing in current_state[current_state[4]]:
            new_state = copy.deepcopy(current_state)
            new_state[new_state[4]].remove(thing)
            new_state[new_state[4]+1].add(thing)
            new_state[4] += 1
            if is_state_valid(new_state) and new_state not in new_states:
                new_states.append(new_state)
        # move 2 things up
        for thing in current_state[current_state[4]]:
            for another_thing in current_state[current_state[4]]:
                if thing != another_thing:
                    new_state = copy.deepcopy(current_state)
                    new_state[new_state[4]].remove(thing)
                    new_state[new_state[4]].remove(another_thing)
                    new_state[new_state[4]+1].add(thing)
                    new_state[new_state[4]+1].add(another_thing)
                    new_state[4] += 1
                    if is_state_valid(new_state) and new_state not in new_states:
                        new_states.append(new_state)

    for checked_state in new_states:
        for state_list in visited_states:
            if checked_state in state_list:
                try:
                    new_states.remove(checked_state)
                except:
                    pass
    return new_states

solved = False
while not solved:
    list_of_current_states = visited_states[-1]
    print(len(visited_states), len(visited_states[-1]))
    possible_next_states = []
    for state in list_of_current_states:
        possible_next_states.extend(find_possible_next_states(state))
    for state in possible_next_states:
        if is_solved(state):
            solved = True
            print("answer:", len(visited_states))
            break
    visited_states.append(possible_next_states)
