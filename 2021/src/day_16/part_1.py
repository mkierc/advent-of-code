from collections import deque

test_stream_list = [
    'D2FE28',
    '38006F45291200',
    'EE00D40C823060',
    '8A004A801A8002F478',
    '620080001611562C8802118E34',
    'C0015000016115A2E0802F182340',
    'A0016C880162017C3686B18A3D4780',
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
    version_sum = 0
    try:
        while _stream:
            x, y, z = _stream.popleft(), _stream.popleft(), _stream.popleft()
            version = int(f'{x}{y}{z}', base=2)
            version_sum += version
            x, y, z = _stream.popleft(), _stream.popleft(), _stream.popleft()
            operator_type = int(f'{x}{y}{z}', base=2)
            if operator_type == 4:
                number = ''
                while _stream.popleft() == '1':  # 1 - not last group
                    a, b, c, d = _stream.popleft(), _stream.popleft(), _stream.popleft(), _stream.popleft()
                    number += hex(int(f'{a}{b}{c}{d}', base=2))
                # 0 - last group
                a, b, c, d = _stream.popleft(), _stream.popleft(), _stream.popleft(), _stream.popleft()
                number += hex(int(f'{a}{b}{c}{d}', base=2))
                break
            else:  # operator packet
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
                        subversion, substream = read_packet(substream)
                        version_sum += subversion
                elif length_type == '1':  # 11 bits
                    a, b, c, d, e, f, g, h, i, j, k = _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                      _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                      _stream.popleft(), _stream.popleft(), _stream.popleft(), \
                                                      _stream.popleft(), _stream.popleft()
                    length = int(f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}', base=2)
                    for i in range(length):
                        subversion, rest = read_packet(_stream)
                        version_sum += subversion
                        _stream = rest
                else:
                    raise BrokenPipeError
                break
    except IndexError:
        pass

    return version_sum, _stream


def main():
    for test_stream in test_stream_list:
        test, _ = read_packet(decode(test_stream))
        print(f"test: {test}")

    answer, rest = read_packet(input_stream)
    print(f"answer: {answer}")


if __name__ == "__main__":
    main()
