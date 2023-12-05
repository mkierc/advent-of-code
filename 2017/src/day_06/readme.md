##  Optimizing the memory bank reallocation

Running with: i7 7700k@4,5GHz

#### Part 1

| Solution \ Run            | 1st       | 2nd       | 3rd       | Average       | Improvement   |
|---------------------------|-----------|-----------|-----------|---------------|---------------|
| Unoptimized               | 1.80981 s | 1.78474 s | 1.78677 s | **1.79378 s** | -             |
| + Tuples                  | 1.68849 s | 1.68848 s | 1.68646 s | **1.68781 s** | **5.9%**      |
| + Index / Max             | 1.63534 s | 1.62933 s | 1.64240 s | **1.63569 s** | **3.1%**      |
| + Constant modulo         | 1.62930 s | 1.62231 s | 1.62231 s | **1.62464 s** | 0.6%          |
| + Set                     | 0.04110 s | 0.04011 s | 0.04110 s | **0.04077 s** | **97.5%**     |

#### Part 2

| Solution \ Run            | 1st       | 2nd       | 3rd       | Average       | Improvement   |
|---------------------------|-----------|-----------|-----------|---------------|---------------|
| Unoptimized               | 9.63359 s | 9.63562 s | 9.56644 s | **9.61188 s** | -             |
| + Tuples                  | 8.41638 s | 8.31210 s | 8.30709 s | **8.34519 s** | **13.1%**     |
| + Index / Max             | 8.31809 s | 8.22390 s | 8.21584 s | **8.25261 s** | 1.1%          |
| + Constant modulo         | 8.24496 s | 8.21484 s | 8.21985 s | **8.22655 s** | 0.3%          |
| + Dictionary              | 0.04411 s | 0.04412 s | 0.04408 s | **0.04410 s** | **99.4%**     |

My first solution to the problem was a quick and naive implementation, using a **list of lists** to
represent the visited states history and redistribtion cycle count:

```
    state = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
    cycle = 0
    ...
    visited_states = [[state, cycle]]
```

That data structure is ineffective, because we don't need to access the individual values of
the state, we're only interested in comparing entire current state to previously visited states.
We're only changing the state while doing the "_data distribution_".

**Tuple** is a data structure very similar to the **list**, but it's better suited for the sake
of puzzle - it's faster to instantiate and has no memory overhead for adding elements like lists do.
And we can easily swap between tuple and list, just by using their respective constructors
on each other.

```
    state = (4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5)
    cycle = 0
    ...
    visited_states = [[state, cycle]]
```

This simple change improved the average execution time from **9.61188 s** to **8.34519 s**,
for a considerable **13.1%** improvement for second part, and **5.9%** for the first part.

---

There's a room for a small improvement, instead of using my wonky implementation of finding
the index of the greatest element:

```
    def find_postion_of_max(state):
        max_value = 0
        position = 0
        for i in range(len(state)):
            if data[i] > max_value:
                max_value = state[i]
                position = i
        return position
```

we can use the simple and fast built-in implementation

```
    state.index(max(state))
```

Also instead of pointlessly calculating the size of state for modulo to wrap around:

```
    source_position = (source_position + 1) % len(state)
```

We can just use a inlined constant

```
    source_position = (source_position + 1) % 16
```

These changes are not that significant, giving us a **8.22655 s** time instead of **8.34519 s**,
that result in a slight **1.4%** improvement for the second part, and oddly a better **3.7%**
improvement for the first part.

---

The greatest bottleneck lies in the way the list of states is accessed; Because we really want to
search through a simple list of states, and the entire structure of state history is a list of lists
containg states, there's an in-between step of unpacking the structure every course of the loop:

```
    visited_states = [[state, cycle]]
    ...
    if state not in list(zip(*visited_states))[0]:
        ...
        return cycle - find_position_in_list(visited_states, state)
```

By using a structure with a faster, straightforward access, it's possible to really go down
on execution time.

```
    visited_states = {state: cycle}
    ...
    if state not in visited_states.keys():
        ...
        return cycle - visited_states.get(state)
```

For both parts of the challenge, we can use respectively:

 * A **set** - when we only need information about whether we visited the state
 * A **dictionary** - for additional information about cycle count for each state in second part

Both of those types need their elements/keys to be immutable, but because we already replaced
**lists** with **tuples**, we've got it covered:

Now the average execution time went down from **8.22655 s** to **0.04410 s**, for a whopping
**99.4%** improvement for the second part and an equally impressive **97.5%** improvement for
the first part.
