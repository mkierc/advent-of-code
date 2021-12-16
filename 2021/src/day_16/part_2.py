from collections import deque

test_stream_list = [
    'C200B40A82',
    '04005AC33890',
    '880086C3E88112',
    'CE00C43D881120',
    'D8005AC2A8F0',
    'F600BC2D8F',
    '9C005AC2F8F0',
    '9C0141080250320F1802104A08',
]

input_stream = ''

with open("data.txt") as file:
    input_data = file.read()
    for digit in input_data:
        input_stream += f'{int(digit, base=16):>04b}'


def decode(_hex_stream):
    output = ''
    for digit in _hex_stream:
        output += f'{int(digit, base=16):>04b}'
    return output


def read_packet(stream):
    _stream = deque(stream)
    operand_list = []
    try:
        while _stream:
            # pop the version tag
            _stream.popleft(), _stream.popleft(), _stream.popleft()
            x, y, z = _stream.popleft(), _stream.popleft(), _stream.popleft()
            operator_type = int(f'{x}{y}{z}', base=2)
            if operator_type == 4:
                number = ''
                while _stream.popleft() == '1':  # 1 - not last group
                    a, b, c, d = _stream.popleft(), _stream.popleft(), _stream.popleft(), _stream.popleft()
                    number += format(int(f'{a}{b}{c}{d}', base=2), 'x')
                # 0 - last group
                a, b, c, d = _stream.popleft(), _stream.popleft(), _stream.popleft(), _stream.popleft()
                number += format(int(f'{a}{b}{c}{d}', base=2), 'x')
                operand_list.append(int(number, base=16))
                break
            else:  # operator packet
                if operator_type == 0:
                    operand_list.append("+")
                elif operator_type == 1:
                    operand_list.append("*")
                elif operator_type == 2:
                    operand_list.append("min")
                elif operator_type == 3:
                    operand_list.append("max")
                elif operator_type == 5:
                    operand_list.append(">")
                elif operator_type == 6:
                    operand_list.append("<")
                elif operator_type == 7:
                    operand_list.append("==")
                length_type = _stream.popleft()
                if length_type == '0':  # 15 bits
                    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                                  _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                                  _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                                  _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                                  _stream.popleft(), _stream.popleft(), _stream.popleft()
                    length = int(f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}', base=2)
                    substream = []
                    for i in range(length):
                        substream += _stream.popleft()

                    while substream:
                        operands, substream = read_packet(substream)
                        operand_list.append(operands)
                elif length_type == '1':  # 11 bits
                    a, b, c, d, e, f, g, h, i, j, k = _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                      _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                      _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                      _stream.popleft(), _stream.popleft()
                    length = int(f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}', base=2)
                    for i in range(length):
                        operands, rest = read_packet(_stream)
                        operand_list.append(operands)
                        _stream = rest
                else:
                    raise BrokenPipeError
                break
    except IndexError:
        pass

    return operand_list, _stream


def calculate(operands):
    if len(operands) == 1:
        return operands[0]
    else:
        operation, *numbers = operands
        if operation == '+':
            _sum = 0
            for number in numbers:
                _sum += calculate(number)
            return _sum
        elif operation == '*':
            _product = 1
            for number in numbers:
                _product *= calculate(number)
            return _product
        elif operation == 'max':
            maximum = []
            for number in numbers:
                maximum.append(calculate(number))
            return max(maximum)
        elif operation == 'min':
            minimum = []
            for number in numbers:
                minimum.append(calculate(number))
            return min(minimum)
        elif operation == '>':
            a = calculate(numbers[0])
            b = calculate(numbers[1])
            if a > b:
                return 1
            else:
                return 0
        elif operation == '<':
            a = calculate(numbers[0])
            b = calculate(numbers[1])
            if a < b:
                return 1
            else:
                return 0
        elif operation == '==':
            a = calculate(numbers[0])
            b = calculate(numbers[1])
            if a == b:
                return 1
            else:
                return 0


def main():
    for test_stream in test_stream_list:
        test = calculate(read_packet(decode(test_stream))[0])
        print(f"test: {test}")

    answer = calculate(read_packet(input_stream)[0])
    print(f"answer: {answer}")


if __name__ == "__main__":
    main()
