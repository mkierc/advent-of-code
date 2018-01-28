test_input_1 = '<>'
test_input_2 = '<random characters>'
test_input_3 = '<<<<>'
test_input_4 = '<{!>}>'
test_input_5 = '<!!>'
test_input_6 = '<!!!>>'
test_input_7 = '<{o"i!a,<{i<a>'

IN_GROUP = '{'
IN_GARBAGE = '<'
ESCAPING = '!'
CLOSE_GROUP = '}'
CLOSE_GARBAGE = '>'

with open("data.txt") as file:
    input_data = file.read()


def parse(stream):
    state_stack = []
    group_counter = 0
    garbage_counter = 0

    for character in stream:
        if not state_stack or state_stack[-1] == IN_GROUP:
            if character == IN_GROUP:
                state_stack.append(IN_GROUP)
                group_counter += state_stack.count('{')
            elif character == IN_GARBAGE:
                state_stack.append(IN_GARBAGE)
            elif character == ESCAPING:
                state_stack.append(ESCAPING)
            elif character == CLOSE_GROUP:
                state_stack.pop()
            else:
                pass
        elif state_stack[-1] == IN_GARBAGE:
            if character == CLOSE_GARBAGE:
                state_stack.pop()
            elif character == ESCAPING:
                state_stack.append(ESCAPING)
            else:
                garbage_counter += 1
        elif state_stack[-1] == ESCAPING:
            state_stack.pop()
        else:
            raise BrokenPipeError(character, state_stack)

    return garbage_counter


def main():
    test_1 = parse(test_input_1)
    print("test_1:", test_1)
    test_2 = parse(test_input_2)
    print("test_2:", test_2)
    test_3 = parse(test_input_3)
    print("test_3:", test_3)
    test_4 = parse(test_input_4)
    print("test_4:", test_4)
    test_5 = parse(test_input_5)
    print("test_5:", test_5)
    test_6 = parse(test_input_6)
    print("test_6:", test_6)
    test_7 = parse(test_input_7)
    print("test_7:", test_7)

    answer = parse(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
