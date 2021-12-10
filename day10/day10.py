matching = {"(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{", "<": ">", ">": "<"}


def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def isOpening(_character):
    return _character == "(" or _character == "[" or _character == "{" or _character == "<"


def isClosing(_character):
    return _character == ")" or _character == "]" or _character == "}" or _character == ">"


def isMatching(_character, _matching):
    return matching[_character] == _matching


def isValid(_data):
    stack = []
    for i in range(len(_data)):
        if isOpening(_data[i]):
            stack.append(_data[i])
        else:
            character = stack.pop()
            if not isMatching(_data[i], character):
                return False, matching[character], _data[i]
    return [True]


def isIncomplete(_data):
    stack = []
    for i in range(len(_data)):
        if isOpening(_data[i]):
            stack.append(_data[i])
        else:
            character = stack.pop()
            if not isMatching(_data[i], character):
                return [False]
    if len(stack) == 0:
        return [False]
    else:
        remaining = ""
        while not len(stack) == 0:
            remaining += matching[stack.pop()]
        return [True, remaining]


def scoreA(_count):
    total = 0
    for key in _count:
        if key == ")":
            total += 3 * _count[key]
        elif key == "]":
            total += 57 * _count[key]
        elif key == "}":
            total += 1197 * _count[key]
        else:
            total += 25137 * _count[key]
    return total


def scoreB(_remaining):
    total = 0
    for i in range(len(_remaining)):
        if _remaining[i] == ")":
            total = (total * 5) + 1
        elif _remaining[i] == "]":
            total = (total * 5) + 2
        elif _remaining[i] == "}":
            total = (total * 5) + 3
        else:
            total = (total * 5) + 4
    return total


def partA(_path):
    data = input(_path)
    counter = {}
    for dataElement in data:
        result = isValid(dataElement)
        if not result[0]:
            if result[2] in counter:
                counter[result[2]] += 1
            else:
                counter[result[2]] = 1
    return scoreA(counter)


def partB(_path):
    data = input(_path)
    counter = []
    for dataElement in data:
        result = isIncomplete(dataElement)
        if result[0]:
            counter.append(scoreB(result[1]))
    return sorted(counter)[int(len(counter) / 2)]


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
