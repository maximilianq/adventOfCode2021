def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(path):
    lines = input(path)[0].split(",")
    output = []
    for line in lines:
        output.append(int(line))
    return output


def decrease(data):
    for i in range(len(data)):
        data[i] -= 1
    return data


def child(data):
    for i in range(len(data)):
        if data[i] == 0:
            data.append(9)
            data[i] = 7
    return data


def process(path):
    data = convert(path)
    for i in range(0, 80):
        data = child(data)
        data = decrease(data)
        print(str(i) + "\t" + str(len(data)))


if __name__ == '__main__':
    process("input.txt")