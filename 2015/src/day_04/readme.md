## Day 4 - The Ideal Stocking Stuffer

### Part One

Santa needs help [mining][3] some AdventCoins (very similar to [bitcoins][4]) to use as gifts
for all the economically forward-thinking little girls and boys.

To do this, he needs to find [MD5][5] hashes which, in [hexadecimal][6], start with at least
**five zeroes**. The input to the MD5 hash is some secret key (your puzzle input, given below)
followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number
(no leading zeroes: `1`, `2`, `3`, ...) that produces such a hash.

For example:

 * If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043`
    starts with five zeroes (`000001dbbfa...`), and it is the lowest such number to do so.
 * If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash starting
    with five zeroes is `1048970`; that is, the MD5 hash of `pqrstuv1048970` looks like
    `000006136ef....`

[Part 1 solution][1]
--------------------

### Part Two



[Part 2 solution][2]
--------------------


[1]: part_1.py
[2]: part_2.py
[3]: https://en.wikipedia.org/wiki/Bitcoin#Mining
[4]: https://en.wikipedia.org/wiki/Bitcoin
[5]: https://en.wikipedia.org/wiki/MD5
[6]: https://en.wikipedia.org/wiki/Hexadecimal
