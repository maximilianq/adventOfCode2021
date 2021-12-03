def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def findO(path):
    _gamma = ""
    lines = input(path)
    for i in range(len(lines[0])):
        counter = 0
        for line in lines:
            if line[i] == "1":
                counter += 1
        _lines = []
        if counter >= (len(lines) / 2):
            _lines = filter(lines, i, "1")
        else:
            _lines = filter(lines, i, "0")
        if len(_lines) > 0:
            lines = _lines
    return int(lines[0], 2)


def findCO(path):
    _gamma = ""
    lines = input(path)
    for i in range(len(lines[0])):
        counter = 0
        for line in lines:
            if line[i] == "1":
                counter += 1
        _lines = []
        if counter >= (len(lines) / 2):
            _lines = filter(lines, i, "0")
        else:
            _lines = filter(lines, i, "1")
        if len(_lines) > 0:
            lines = _lines
    return int(lines[0], 2)


def filter(input, index, value):
    output = []
    for line in input:
        if line[index] == value:
            output.append(line)
    return output


if __name__ == '__main__':
    print(findO("input.txt") * findCO("input.txt"))
