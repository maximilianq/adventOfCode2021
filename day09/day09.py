def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(path):
    lines = input(path)
    output = []
    for line in lines:
        values = []
        for i in range(len(line)):
            values.append(int(line[i]))
        output.append(values)
    return output


def adjacentHigher(_data, _x, _y):
    output = True
    if 0 < _x:
        if _data[_y][_x - 1] <= _data[_y][_x]:
            output = False
    if len(_data[_y]) - 1 > _x:
        if _data[_y][_x + 1] <= _data[_y][_x]:
            output = False
    if 0 < _y:
        if _data[_y - 1][_x] <= _data[_y][_x]:
            output = False
    if len(_data) - 1 > _y:
        if _data[_y + 1][_x] <= _data[_y][_x]:
            output = False
    return output


def partA(_path):
    data = convert(_path)
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if adjacentHigher(data, j, i):
                total += data[i][j] + 1
    return total


def basin(_data, _x, _y):
    if _data[_y][_x] == 9 or _data[_y][_x] == -1:
        return 0
    else:
        _data[_y][_x] = -1

    size = 1

    if 0 < _x:
        size += basin(_data, _x - 1, _y)
    if len(_data[_y]) - 1 > _x:
        size += basin(_data, _x + 1, _y)
    if 0 < _y:
        size += basin(_data, _x, _y - 1)
    if len(_data) - 1 > _y:
        size += basin(_data, _x, _y + 1)

    return size


def partB(_path):
    data = convert(_path)
    basins = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            size = basin(data, x, y)
            if size > 0:
                basins.append(size)
    basins = sorted(basins, reverse=True)
    return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
