## Day 2 - Corruption Checksum
### Part One

As you walk through the door, a glowing humanoid shape yells in your
direction. "You there! Your state appears to be idle. Come help us
repair the corruption in this spreadsheet - if we take another
millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make
sure the recovery process is on the right track, they need you t
calculate the spreadsheet's **checksum**. For each row, determine
the difference between the largest value and the smallest value;
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

```
5 1 9 5
7 5 3
2 4 6 8
```

 * The first row's largest and smallest values are `9` and `1`,
   and their difference is `8`.
 * The second row's largest and smallest values are `7` and `3`,
   and their difference is `4`.
 * The third row's difference is 6.

In this example, the spreadsheet's checksum would be `8 + 4 + 6 = 18`.

**What is the checksum** for the spreadsheet in your puzzle input?


[Part 1 solution][1]
--------------------


You notice a progress bar that jumps to 50% completion. Apparently,
the door isn't yet satisfied, but it did emit a **star** as
encouragement. The instructions change:

Now, instead of considering the **next** digit, it wants you to consider
the digit **halfway around** the circular list. That is, if your list
contains `10` items, only include a digit in your sum if the digit
`10/2 = 5` steps forward matches it. Fortunately, your list has an even
number of elements.

For example:

 * `1212` produces `6`: the list contains `4` items, and all four digits
   match the digit `2` items ahead.
 * `1221` produces `0`, because every comparison is between a `1`
   and a `2`.
 * `123425` produces `4`, because both 2s match each other, but no other
   digit has a match.
 * `123123` produces `12`.
 * `12131415` produces `4`.

**What is the solution** to your new captcha?

[Part 2 solution][2]
--------------------


[1]: part_1.py
[2]: part_2.py
