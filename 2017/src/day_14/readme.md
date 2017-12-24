## Day 14 - Disk Defragmentation

### Part One

Suddenly, a scheduled job activates the system's [disk defragmenter][3]. Were the situation
different, you might [sit and watch it for a while][4], but today, you just don't have that
kind of time. It's soaking up valuable system resources that are needed elsewhere, and so
the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either **free**
or **used**. On this disk, the state of the grid is tracked by the bits in a sequence
of [knot hashes][5].

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid;
each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash
indicates whether that square is **free** (`0`) or **used** (`1`).

The hash inputs are a key string (your puzzle input), a dash, and a number from `0` to `127`
corresponding to the row. For example, if your key string were `flqrgnkx`, then the first row
would be given by the bits of the knot hash of `flqrgnkx-0`, the second row from the bits
of the knot hash of `flqrgnkx-1`, and so on until the last row, `flqrgnkx-127`.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these
digits correspond to 4 bits, for a total of `4 * 32 = 128` bits. To convert to bits, turn each
hexadecimal digit to its equivalent binary value, high-bit first: `0` becomes `0000`,
`1` becomes `0001`, `e` becomes `1110`, `f` becomes `1111`, and so on; a hash that begins
with `a0c2017...` in hexadecimal would begin with `10100000110000100000000101110000...` in binary.

Continuing this process, the **first 8 rows and columns** for key `flqrgnkx` appear as follows,
using `#` to denote used squares, and `.` to denote free ones:

```
##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V
```

In this example, `8108` squares are used across the entire 128x128 grid.

Given your actual key string, **how many squares are used**?

[Part 1 solution][1]
--------------------

### Part Two

[Part 2 solution][2]
--------------------


[1]: part_1.py
[2]: part_2.py
[3]: https://en.wikipedia.org/wiki/Defragmentation
[4]: https://www.youtube.com/watch?v=kPv1gQ5Rs8A&t=37
[5]: ../day_10