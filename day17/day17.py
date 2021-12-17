def read(_path):
    lines = []
    with open(_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    _data = read(_path)[0]
    [_width, _height] = _data.replace("target area: x=", "").split(", y=")
    width = [int(_width.split("..")[0]), int(_width.split("..")[1])]
    height = [int(_height.split("..")[0]), int(_height.split("..")[1])]
    return [width, height]


def inTarget(_location, _target):
    return _target[0][0] <= _location[0] <= _target[0][1] and _target[1][0] <= _location[1] <= _target[1][1]


def reachTarget(_location, _velocity, _target):
    return True in calcLocations(_location, _velocity, _target).values()


def calcHeight(_location, _velocity, _target):
    return max([loc[1] for loc in calcLocations(_location, _velocity, _target).keys()])


def calcLocations(_location, _velocity, _target):
    locations = {(_location[0], _location[1]): inTarget(_location, _target)}

    while _location[0] <= _target[0][1] and _location[1] >= _target[1][0]:
        _location = [loc + vel for loc, vel in zip(_location, _velocity)]
        _velocity[0] = max(_velocity[0] - 1, 0)
        _velocity[1] = _velocity[1] - 1
        locations[(_location[0], _location[1])] = inTarget(_location, _target)

    return locations


def partA(_path):
    target = convert(_path)

    location = [0, 0]

    maxHeight = None

    for _y in range(-1000, 1000):
        for _x in range(0, 1000):
            if reachTarget(location, [_x, _y], target):
                _height = calcHeight(location, [_x, _y], target)
                if maxHeight is None or _height > maxHeight:
                    maxHeight = _height

    return maxHeight


def partB(_path):
    target = convert(_path)

    location = [0, 0]

    count = 0

    for _y in range(-1000, 1000):
        for _x in range(0, 1000):
            if reachTarget(location, [_x, _y], target):
                count += 1

    return count


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
