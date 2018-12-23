def run_assembly():
    h = 0                           # "all start at 0"
    # a = 1                         # "a now start at 0"    NOP

    b = 67                          # set b 67
    # c = b                         # set c b               NOP

    # if a != 0:                    # jnz a 2               NOP
    #                               # jnz 1 5               NOP

    b = b * 100                     # mul b 100
    b = b + 100000                  # sub b -100000
    c = b                           # set c b
    c = c + 17000                   # sub c -17000

    while True:                     # LABEL_ONE
        f = 1                       # set f 1
        d = 2                       # set d 2

        # e = 2                     # set e 2               NOP
        # g = d                     # set g d               NOP

        while True:                 # LABEL_TWO
            #                       # mul g e
            #                       # sub g b
            if b % d == 0:          # jnz g 2
                f = 0               # set f 0

            # e = e + 1             # sub e -1              NOP

            #                       # set g e               NOP
            # if b == e:            # sub g b               NOP
            #     continue          # jnz g -8              NOP

            d = d + 1               # sub d -1

            #                       # set g d
            if d != b:              # sub g b
                continue            # jnz g -13             jump to LABEL_TWO

            if f == 0:              # jnz f 2
                h = h + 1           # sub h -1

            #                       # set g b
            #                       # sub g c
            if b == c:              # jnz g 2
                return h            # jnz 1 3               jump outside (return)
            else:
                b = b + 17          # sub b -17
                break               # jnz 1 -23             jump to LABEL_ONE


def main():
    answer = run_assembly()
    print("answer:", answer)


if __name__ == "__main__":
    main()
