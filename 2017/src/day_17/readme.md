## Day 17 - Spinlock

### Part One

Suddenly, whirling in the distance, you notice what looks like a massive, pixelated hurricane:
a deadly [spinlock][3]. This spinlock isn't just consuming computing power, but memory, too;
vast, digital mountains are being ripped from the ground and consumed by the vortex.

If you don't move quickly, fixing that printer will be the least of your problems.

This spinlock's algorithm is simple but efficient, quickly consuming everything in its path.
It starts with a circular buffer containing only the value `0`, which it marks as
the **current position**. It then steps forward through the circular buffer some number of steps
(your puzzle input) before inserting the first new value, `1`, after the value it stopped on.
The inserted value becomes the **current position**. Then, it steps forward from there
the same number of steps, and wherever it stops, inserts after it the second new value, `2`,
and uses that as the new **current position** again.

It repeats this process of **stepping forward**, **inserting a new value**, and **using the location
of the inserted value as the new current position** a total of **`2017`** times, inserting `2017`
as its final operation, and ending with a total of `2018` values (including `0`) in
the circular buffer.

For example, if the spinlock were to step `3` times per insert, the circular buffer would begin
to evolve like this (using parentheses to mark the current position after each iteration of
the algorithm):

 * `(0)`, the initial state before any insertions.
 * `0 (1)`: the spinlock steps forward three times (`0`, `0`, `0`), and then inserts
    the first value, `1`, after it. `1` becomes the current position.
 * `0 (2) 1`: the spinlock steps forward three times (`0`, `1`, `0`), and then inserts
    the second value, `2`, after it. `2` becomes the current position.
 * `0  2 (3) 1`: the spinlock steps forward three times (`1`, `0`, `2`), and then inserts
    the third value, `3`, after it. `3` becomes the current position.

And so on:

 * `0  2 (4) 3  1`
 * `0 (5) 2  4  3  1`
 * `0  5  2  4  3 (6) 1`
 * `0  5 (7) 2  4  3  6  1`
 * `0  5  7  2  4  3 (8) 6  1`
 * `0 (9) 5  7  2  4  3  8  6  1`

Eventually, after 2017 insertions, the section of the circular buffer near the last insertion
looks like this:

```
1512  1134  151 (2017) 638  1513  851
```

Perhaps, if you can identify the value that will ultimately be **after** the last value written
(`2017`), you can short-circuit the spinlock. In this example, that would be `638`.

**What is the value after `2017`** in your completed circular buffer?

[Part 1 solution][1]
--------------------

### Part Two

The spinlock does not short-circuit. Instead, it gets **more** angry. At least, you assume that's
what happened; it's spinning significantly faster than it was a moment ago.

You have good news and bad news.

The good news is that you have improved calculations for how to stop the spinlock. They indicate
that you actually need to identify **the value after `0`** in the current state of
the circular buffer.

The bad news is that while you were determining this, the spinlock has just finished inserting
its fifty millionth value (`50000000`).

**What is the value after `0`** the moment `50000000` is inserted?

[Part 2 solution][2]
--------------------

## Optimization of Part 2

Running with: i7 7700k@4,5GHz

I've began with estimating the memory requirement of the naive implementation:

| Structure                                 |          size |   s/1024/1024 |
|:------------------------------------------|--------------:|--------------:|
| Empty list                                |          64 B |             - |
| 1 int                                     |           8 B |             - |
| 50 000 001 ints + list                    |   400000072 B |     381.46 MB |
| List of 50 000 001 ints + list overhead   |   424076264 B | **404.43 MB** |

The entire number list would need a little bit over **400 MB**, so it's not a big deal.

Time requirement however, is insanely long - the extrapolated time requirement was **over 60 days**.

To extrapolate, I've generated first `200 000` states, measuring time elapsed between every `10 000`
generated states using:

```
start_time = time.time()

    ...
    if i % 10000 == 0:
        print(i, time.time() - start_time)
    ...
```

Doing that I've acquired some data points for the extrapolation:

|    States |  Elapsed time |
|----------:|--------------:|
|     10000 |   0.2717514 s |
|     20000 |   1.1400308 s |
|     30000 |   2.6085634 s |
|     40000 |   4.6817502 s |
|     50000 |   7.3493192 s |
|     60000 |  10.6131870 s |
|     70000 |  14.4811995 s |
|     80000 |  18.9508862 s |
|     90000 |  24.0068151 s |
|    100000 |  29.7068729 s |
|    110000 |  35.9707674 s |
|    120000 |  42.8768818 s |
|    130000 |  50.3933198 s |
|    140000 |  58.5908844 s |
|    150000 |  67.4257111 s |
|    160000 |  76.9266819 s |
|    170000 |  87.0808138 s |
|  *200000* |*121.8512763 s*|

I've solved a **second order polynomial regression function** over 17 data points (20th point was
for cross-validation of formula):

```
y = 3.071247227 * 10^(-9) * x^2 - 1.210640658 * 10^(-5) * x + 1.988593495 * 10^(-1)
```

I've implemented the function in Python and calculated the 20th data point for cross-validation:

```
>>> def y(x):
...     return 3.071247227 * 10**(-9) * x**2 - 1.210640658 * 10**(-5) * x + 1.988593495 * 10**(-1)
...
>>> y(200000)
120.6274671135
```

It's fairly close, off by **1.2238 s** from the real value, so my extrapolation function is
*underestimating* by about **1.0145%**. Good enough for me.

![Extrapolation plot](extrapolation_plot.png)

<sup>[Plotting code][3]</sup>

Now to calculate the time for entire length of the input:

```
>>> y(50000001)
7677513.25314297
```

...which yields **7677513.25 seconds**, in sane units: **88 days 20 hours 38 minutes 33 seconds**.

Running it for a few months was obviously out of question.

---

Acorrding to the puzzle description, the program should "*insert the new value, **after** the value
it stopped on*", so it we can deduce that it will never put a new value on the `0th` index,
and so the value `0` will stay there indefinitely.

We'll test that by modyfing solution of Part 1...

```
    ...
        if i <= 20:
            print(i, numbers)
    ...
```

...and taking a look at first 20 states:

```
1 [0, 1]
2 [0, 2, 1]
3 [0, 2, 3, 1]
4 [0, 2, 4, 3, 1]
5 [0, 5, 2, 4, 3, 1]
6 [0, 5, 2, 4, 3, 6, 1]
7 [0, 5, 2, 4, 3, 7, 6, 1]
8 [0, 8, 5, 2, 4, 3, 7, 6, 1]
9 [0, 8, 5, 2, 4, 9, 3, 7, 6, 1]
10 [0, 8, 5, 2, 4, 9, 3, 7, 6, 10, 1]
11 [0, 8, 5, 2, 4, 9, 3, 7, 6, 10, 11, 1]
12 [0, 8, 12, 5, 2, 4, 9, 3, 7, 6, 10, 11, 1]
13 [0, 8, 13, 12, 5, 2, 4, 9, 3, 7, 6, 10, 11, 1]
14 [0, 8, 14, 13, 12, 5, 2, 4, 9, 3, 7, 6, 10, 11, 1]
15 [0, 8, 14, 13, 12, 5, 15, 2, 4, 9, 3, 7, 6, 10, 11, 1]
16 [0, 8, 16, 14, 13, 12, 5, 15, 2, 4, 9, 3, 7, 6, 10, 11, 1]
17 [0, 8, 16, 14, 13, 12, 5, 15, 2, 17, 4, 9, 3, 7, 6, 10, 11, 1]
18 [0, 8, 16, 14, 13, 12, 5, 15, 2, 17, 4, 9, 3, 18, 7, 6, 10, 11, 1]
19 [0, 8, 16, 14, 13, 12, 5, 15, 2, 17, 4, 9, 3, 18, 7, 6, 19, 10, 11, 1]
20 [0, 8, 16, 14, 13, 12, 5, 15, 2, 17, 4, 9, 3, 18, 7, 6, 19, 10, 11, 1, 20]
```

Indeed that seems to be the case. Now that we know that, we can completely omit construction of
the number list, as well as inserting consecutive values at their respective position, and just
keep track of the values that are inserted at the `1st` position.

Now the solution runs in **4.88938 s**, about **1 570 243 times** faster! Now that's what I call a
successful optimization!


[1]: part_1.py
[2]: part_2.py
[3]: https://en.wikipedia.org/wiki/Spinlock
[4]: extrapolation.py
