def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    lines = input(_path)
    output = {}
    for line in lines:
        [start, stop] = line.split("-")
        if start in output:
            output[start].append(stop)
        else:
            output[start] = [stop]
        if stop in output:
            output[stop].append(start)
        else:
            output[stop] = [start]
    return output


def checkA(_initial, _previous):
    return _initial.islower() and _initial in _previous


def calculateA(_data, _initial, _previous):

    if _initial == "end":
        _previous.append("end")
        return [_previous]

    if checkA(_initial, _previous):
        return []

    _previous.append(_initial)

    output = []

    for _dest in _data[_initial]:
        for option in calculateA(_data, _dest, _previous.copy()):
            output.append(option)

    return output


def checkB(_initial, _previous):

    if "start" in _previous and _initial == "start":
        return True

    _frequency = frequencyLower(_previous)

    if 2 in _frequency.values():
        return _initial.islower() and _initial in _previous
    else:
        return False


def frequencyLower(_data):
    output = {}
    for data in _data:
        if data.islower():
            if data in output:
                output[data] += 1
            else:
                output[data] = 1
    return output


def calculateB(_data, _initial, _previous):

    if _initial == "end":
        _previous.append("end")
        return [_previous]

    if checkB(_initial, _previous):
        return []

    _previous.append(_initial)

    output = []

    for _dest in _data[_initial]:
        for option in calculateB(_data, _dest, _previous.copy()):
            output.append(option)

    return output


def partA(_path):
    data = convert(_path)
    result = calculateA(data, "start", [])

    for _result in result:
        print(_result)

    return result


def partB(_path):
    data = convert(_path)
    result = calculateB(data, "start", [])

    for _result in result:
        print(_result)

    return result


if __name__ == '__main__':
    print(len(partA("input.txt")))
    print(len(partB("input.txt")))
