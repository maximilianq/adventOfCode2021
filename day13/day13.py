def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    lines = input(_path)

    data = []
    instruction = []

    row = False

    for line in lines:
        if line == "":
            row = True
        else:
            if not row:
                split = line.split(",")
                data.append([int(split[0]), int(split[1])])
            else:
                split = line.replace("fold along ", "").split("=")
                instruction.append([split[0], int(split[1])])

    return [data, instruction]


def size(_data):
    xmax = 0
    ymax = 0
    for data in _data:
        xmax = max(xmax, data[0])
        ymax = max(ymax, data[1])
    return [xmax + 1, ymax + 1]


def offset(_data):
    xmin = 0
    ymin = 0
    for data in _data:
        xmin = min(xmin, data[0])
        ymin = min(ymin, data[1])
    return [xmin, ymin]


def foldY(_data, _height, _y):
    data = []
    for [x, y] in _data:
        dx = x
        dy = y if y < _y else (2 * _y) - y
        data.append([dx, dy])
    yOffset = max(-1 * offset(data)[1], 0)
    for i in range(len(data)):
        data[i] = [data[i][0], data[i][1] + yOffset]
    return [data, _y if 2 * _y > _height else _height - _y - 1]


def foldX(_data, _width, _x):
    data = []
    for [x, y] in _data:
        dx = x if x < _x else (2 * _x) - x
        dy = y
        data.append([dx, dy])
    xOffset = max(-1 * offset(data)[0], 0)
    for i in range(len(data)):
        data[i] = [data[i][0] + xOffset, data[i][1]]
    return [data, _x if 2 * _x > _width else _width - _x - 1]


def printMatrix(_data, _width, _height):

    for y in range(_height):
        for x in range(_width):
            if [x, y] in _data:
                print("x", end="")
            else:
                print(".", end="")
        print("")


def count(_data):
    unique = []
    for data in _data:
        if data not in unique:
            unique.append(data)
    return len(unique)


def partA(_path):
    [data, instructions] = convert(_path)
    [width, height] = size(data)

    if instructions[0][0] == "x":
        result = foldX(data, width, instructions[0][1])
        data = result[0]
    else:
        result = foldY(data, height, instructions[0][1])
        data = result[0]
    print(count(data))


def partB(_path):
    [data, instructions] = convert(_path)
    [width, height] = size(data)

    for instruction in instructions:
        if instruction[0] == "x":
            result = foldX(data, width, instruction[1])
            data = result[0]
            width = result[1]
        else:
            result = foldY(data, height, instruction[1])
            data = result[0]
            height = result[1]
    printMatrix(data, width, height)


if __name__ == '__main__':
    partA("input.txt")
    partB("input.txt")
