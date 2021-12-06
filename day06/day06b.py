def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(path):
    lines = input(path)[0].split(",")

    temp = []
    for line in lines:
        temp.append(int(line))

    output = {}
    for tempElement in temp:
        if tempElement in output:
            output[tempElement] += 1
        else:
            output[tempElement] = 1

    return output


def decrease(data):
    output = {}
    for key in data.keys():
        output[key - 1] = data[key]
    return output


def child(data):
    output = {}
    for key in data.keys():
        if key == 0:
            if 7 in output:
                output[7] = output[7] + data[key]
            else:
                output[7] = data[key]
            if 9 in output:
                output[9] += data[key]
            else:
                output[9] = data[key]
        else:
            if key in output.keys():
                output[key] = output[key] + data[key]
            else:
                output[key] = data[key]
    return output


def length(data):
    count = 0
    for key in data.keys():
        count += data[key]
    return count


def process(path):
    data = convert(path)
    for i in range(0, 256):
        data = child(data)
        data = decrease(data)
    print(length(data))


if __name__ == '__main__':
    process("input.txt")