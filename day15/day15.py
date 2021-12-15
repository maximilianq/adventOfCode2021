import sys
from queue import PriorityQueue


def read(_path):
    lines = []
    with open(_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    lines = read(_path)
    data = []
    for line in lines:
        _data = []
        for index in range(len(line)):
            _data.append((int(line[index]), False))
        data.append(_data)
    return data


def extend(_data):
    matrix = []
    for _y in range(5):
        for y in range(len(_data)):
            _matrix = []
            for _x in range(5):
                for x in range(len(_data[0])):
                    value = _data[y][x][0] + _x + _y
                    value = value if value <= 9 else value - 9
                    _matrix.append((value, False))
            matrix.append(_matrix)
    return matrix


def neighbours(_data, _x, _y):
    output = []
    if _x > 0 and not _data[_y][_x - 1][1]:
        output.append((_x - 1, _y))
    if _x < len(_data[0]) - 1 and not _data[_y][_x + 1][1]:
        output.append((_x + 1, _y))
    if _y > 0 and not _data[_y - 1][_x][1]:
        output.append((_x, _y - 1))
    if _y < len(_data[0]) - 1 and not _data[_y + 1][_x][1]:
        output.append((_x, _y + 1))
    return output


def path(_data, _x, _y):
    matrix = []
    for y in range(len(_data)):
        _matrix = []
        for x in range(len(_data[y])):
            _matrix.append(sys.maxsize)
        matrix.append(_matrix)
    matrix[0][0] = 0

    queue = PriorityQueue()

    queue.put((0, (0, 0)))

    while not queue.empty():
        [prio, item] = queue.get()
        edges = neighbours(_data, item[0], item[1])
        for edge in edges:
            newValue = matrix[item[1]][item[0]] + _data[edge[1]][edge[0]][0]
            if newValue < matrix[edge[1]][edge[0]]:
                matrix[edge[1]][edge[0]] = newValue
                queue.put((newValue, edge))
        _data[item[1]][item[0]] = (_data[item[1]][item[0]][0], True)
    return matrix[len(matrix) - 1][len(matrix[0]) - 1]


def partA(_path):
    data = convert(_path)
    return path(data, 0, 0)


def partB(_path):
    data = convert(_path)
    matrix = extend(data)
    return path(matrix, 0, 0)


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
