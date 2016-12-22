# 0 = generator
# 1 = microchip
# 0-4 = type
import copy
from time import time
start_time = time()


class State:
    def __init__(self, elevator: int, floors: list):
        self.elevator = elevator
        self.floors = floors

    def is_solved(self):
        """
            x == frozenset()
        is ~1.41 times faster than
            x == set()
        after testing for 100000 tries with timeit:
            import timeit
            a = timeit.timeit("plok == set()", setup="plok = set()", number=100000)
            b = timeit.timeit("plok == frozenset()", setup="plok = set()", number=100000)
            print(a, b, a / b)
        """
        return self.floors[0] == frozenset() \
               and self.floors[1] == frozenset() \
               and self.floors[2] == frozenset()

    @staticmethod
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

    @staticmethod
    def are_valid(old_floor, new_floor):
        return State.is_floor_valid(old_floor) \
               and State.is_floor_valid(new_floor)

    def __repr__(self):
        e = str(self.elevator)
        f = self.floors
        out = "----------------------------------------------------------------------------\n"
        out += "E 3: " if e == "3" else "  3: "
        out += str(f[3]) + "\n"
        out += "E 2: " if e == "2" else "  2: "
        out += str(f[2]) + "\n"
        out += "E 1: " if e == "1" else "  1: "
        out += str(f[1]) + "\n"
        out += "E 0: " if e == "0" else "  0: "
        out += str(f[0]) + "\n"
        out += "==========================================================================="
        return out

    # TODO find a faster/cheaper method to hash state
    def __hash__(self, *args, **kwargs):
        return hash((self.elevator, tuple(tuple(sorted(x)) for x in self.floors)))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return hash(self) != hash(other)


actual_initial_state = State(
    0, [
        {(0, 0), (1, 0)},
        {(0, 1), (0, 2), (0, 3), (0, 4)},
        {(1, 1), (1, 2), (1, 3), (1, 4)},
        set()
    ]
)
test_initial_state = State(
    0, [
        {(1, 1), (1, 0)},
        {(0, 0)},
        {(0, 1)},
        set()
    ]
)


step = 1
visited_states = {test_initial_state}
states_of_last_step = {test_initial_state}


# TODO measure the cost of this method
def find_possible_next_states(current_state: State):
    new_states = set()
    # try moving things down
    if current_state.elevator != 0:  # lowest floor
        # move 1 thing down
        for thing in current_state.floors[current_state.elevator]:
            # TODO find some cheaper method to generate a copy of state
            new_state = copy.deepcopy(current_state)
            new_state.floors[new_state.elevator].remove(thing)
            new_state.elevator -= 1
            new_state.floors[new_state.elevator].add(thing)
            if State.are_valid(new_state.floors[new_state.elevator + 1], new_state.floors[new_state.elevator]) \
                    and new_state not in visited_states:
                new_states.add(new_state)
        # move 2 things down
        # TODO generate new states in a way, that it doesn't generate duplicates like (A, B)&(B, A), (A, A), (B, B)
        for thing in current_state.floors[current_state.elevator]:
            for another_thing in current_state.floors[current_state.elevator]:
                if thing != another_thing:
                    new_state = copy.deepcopy(current_state)
                    new_state.floors[new_state.elevator].remove(thing)
                    new_state.floors[new_state.elevator].remove(another_thing)
                    new_state.elevator -= 1
                    new_state.floors[new_state.elevator].add(thing)
                    new_state.floors[new_state.elevator].add(another_thing)
                    if State.are_valid(new_state.floors[new_state.elevator + 1], new_state.floors[new_state.elevator]) \
                            and new_state not in visited_states:
                        new_states.add(new_state)
    # try moving things up
    if current_state.elevator != 3:  # highest floor
        # move 1 thing up
        for thing in current_state.floors[current_state.elevator]:
            new_state = copy.deepcopy(current_state)
            new_state.floors[new_state.elevator].remove(thing)
            new_state.elevator += 1
            new_state.floors[new_state.elevator].add(thing)
            if State.are_valid(new_state.floors[new_state.elevator - 1], new_state.floors[new_state.elevator]) \
                    and new_state not in visited_states:
                new_states.add(new_state)
        # move 2 things up
        for thing in current_state.floors[current_state.elevator]:
            for another_thing in current_state.floors[current_state.elevator]:
                if thing != another_thing:
                    new_state = copy.deepcopy(current_state)
                    new_state.floors[new_state.elevator].remove(thing)
                    new_state.floors[new_state.elevator].remove(another_thing)
                    new_state.elevator += 1
                    new_state.floors[new_state.elevator].add(thing)
                    new_state.floors[new_state.elevator].add(another_thing)
                    if State.are_valid(new_state.floors[new_state.elevator - 1], new_state.floors[new_state.elevator]) \
                            and new_state not in visited_states:
                        new_states.add(new_state)
    return new_states


solved = False
while not solved:
    print(step, len(states_of_last_step))
    possible_next_states = set()

    # TODO find how to parallelize generation of new states
    for state in states_of_last_step:
        possible_next_states = possible_next_states.union(find_possible_next_states(state))
    for state in possible_next_states:
        if state.is_solved():
            solved = True
            print("answer:", step, end="")
            break

    visited_states = visited_states.union(possible_next_states)
    states_of_last_step = possible_next_states
    step += 1

print(", solved in", time() - start_time, "s")
# test_input takes ~0.17 s
