def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    lines = input(_path)
    output = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            row.append(int(lines[y][x]))
        output.append(row)
    return output


def increase(_data):
    for y in range(len(_data)):
        for x in range(len(_data[y])):
            _data[y][x] += 1
    return _data


def update(_data, _x, _y):

    for y in range(max(_y - 1, 0), min(_y + 1, len(_data) - 1) + 1):
        for x in range(max(_x - 1, 0), min(_x + 1, len(_data[_y]) - 1) + 1):
            if _data[y][x] > 0:
                _data[y][x] += 1

    return _data


def flash(_data, _x, _y, _flash):

    if _data[_y][_x] <= 9:
        return [_data, _flash]

    _data[_y][_x] = 0
    _data = update(_data, _x, _y)
    _flash += 1

    for y in range(max(_y - 1, 0), min(_y + 1, len(_data) - 1) + 1):
        for x in range(max(_x - 1, 0), min(_x + 1, len(_data[_y]) - 1) + 1):
            result = flash(_data, x, y, _flash)
            _data = result[0]
            _flash = result[1]

    return [_data, _flash]


def isSync(_data):
    for y in range(len(_data)):
        for x in range(len(_data[y])):
            if _data[0][0] != _data[y][x]:
                return False
    return True


def prin(_data):
    for data in _data:
        print(data)


def partA(_path):
    data = convert(_path)
    flashes = 0
    for i in range(0, 100):
        data = increase(data)
        for y in range(len(data)):
            for x in range(len(data[y])):
                [data, flashes] = flash(data, x, y, flashes)
    return flashes


def partB(_path):
    data = convert(_path)
    counter = 0
    while not isSync(data):
        counter += 1
        data = increase(data)
        for y in range(len(data)):
            for x in range(len(data[y])):
                data = flash(data, x, y, 0)[0]
    return counter


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
