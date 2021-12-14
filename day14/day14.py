def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    lines = input(_path)
    data = {}
    rules = {}
    row = False
    for line in lines:
        if line == "":
            row = True
        else:
            if not row:
                line += "$"
                for i in range(len(line) - 1):
                    if (line[i], line[i+1]) in data:
                        data[(line[i], line[i+1])] += 1
                    else:
                        data[(line[i], line[i+1])] = 1
            else:
                [marker, replacement] = line.split(" -> ")
                rules[list(marker)[0], list(marker)[1]] = replacement
    return [data, rules]


def count(_data):
    keys = _data.keys()

    symbols = []
    for key in keys:
        symbols.append(key[0])

    occurences = {}

    for key in keys:
        if key[0] in occurences:
            occurences[key[0]] += _data[key]
        else:
            occurences[key[0]] = _data[key]

    return occurences


def partA(_path):
    [data, rules] = convert(_path)

    for iteration in range(10):
        _data = {}
        for key in data.keys():
            if key in rules:
                if (key[0], rules[key]) not in _data:
                    _data[(key[0], rules[key])] = data[key]
                else:
                    _data[(key[0], rules[key])] += data[key]
                if (rules[key], key[1]) not in _data:
                    _data[(rules[key], key[1])] = data[key]
                else:
                    _data[(rules[key], key[1])] += data[key]
            else:
                _data[key] = data[key]
        data = _data

    occurences = count(data)
    return max(occurences.values()) - min(occurences.values())


def partB(_path):
    [data, rules] = convert(_path)

    for iteration in range(40):
        _data = {}
        for key in data.keys():
            if key in rules:
                if (key[0], rules[key]) not in _data:
                    _data[(key[0], rules[key])] = data[key]
                else:
                    _data[(key[0], rules[key])] += data[key]
                if (rules[key], key[1]) not in _data:
                    _data[(rules[key], key[1])] = data[key]
                else:
                    _data[(rules[key], key[1])] += data[key]
            else:
                _data[key] = data[key]
        data = _data

    occurences = count(data)
    return max(occurences.values()) - min(occurences.values())


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
