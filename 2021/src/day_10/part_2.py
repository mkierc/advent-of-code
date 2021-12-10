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
    lines_to_fix = []
    state_stack = []
    error_counter = 0
    for line in stream:
        line_broken = False
        for character in line:
            if not state_stack or character in OPENING:
                state_stack.append(character)
            elif character in CLOSING:
                if state_stack[-1] == OPENING[CLOSING.index(character)]:
                    state_stack.pop()
                else:
                    line_broken = True
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
        if not line_broken:
            lines_to_fix.append(line)
        state_stack = []

    scores = []
    for line in lines_to_fix:
        score = 0
        for character in line:
            if not state_stack or character in OPENING:
                state_stack.append(character)
            elif character in CLOSING:
                state_stack.pop()
        while state_stack:
            matching_character = CLOSING[OPENING.index(state_stack.pop())]
            line += matching_character
            if matching_character == ')':
                score = score * 5 + 1
            elif matching_character == ']':
                score = score * 5 + 2
            elif matching_character == '}':
                score = score * 5 + 3
            elif matching_character == '>':
                score = score * 5 + 4
        scores.append(score)

    return sorted(scores)[int(len(scores)/2)]


def main():
    test = parse(test_input)
    print("test:", test)

    answer = parse(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
