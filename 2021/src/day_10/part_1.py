good_inputs = ['()', '[]', '([])', '{()()()}', '<([{}])>', '[<>({}){}[([])<>]]', '(((((((((())))))))))']
bad_inputs = ['(]', '{()()()>', '(((()))}', '<([]){()}[{}])']

test_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]

OPENING = ['{', '[', '(', '<']
CLOSING = ['}', ']', ')', '>']

with open("data.txt") as file:
    input_data = file.read().splitlines()


def parse(stream):
    state_stack = []
    error_counter = 0
    for line in stream:
        for character in line:
            if not state_stack or character in OPENING:
                state_stack.append(character)
            elif character in CLOSING:
                if state_stack[-1] == OPENING[CLOSING.index(character)]:
                    state_stack.pop()
                else:
                    if character == ')':
                        error_counter += 3
                    elif character == ']':
                        error_counter += 57
                    elif character == '}':
                        error_counter += 1197
                    elif character == '>':
                        error_counter += 25137
                    break
            else:
                raise BrokenPipeError(character, state_stack)
        state_stack = []
    return error_counter


def main():
    test_good = parse(good_inputs)
    print("test_good:", test_good)

    test_bad = parse(bad_inputs)
    print("test_bad:", test_bad)

    test = parse(test_input)
    print("test:", test)

    answer = parse(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
