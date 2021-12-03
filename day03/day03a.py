def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def find(path):
    _gamma = ""
    lines = input(path)
    occurrences = [0] * len(lines[0])
    for line in lines:
        for i in range(len(line)):
            if line[i] == "1":
                occurrences[i] += 1
    for i in range(len(occurrences)):
        if occurrences[i] > (len(lines) / 2):
            _gamma += "1"
        else:
            _gamma += "0"
    _epsilon = invert(_gamma)
    return int(_gamma, 2), int(_epsilon, 2)


def invert(input):
    output = "";
    for i in range(len(input)):
        if input[i] == "1":
            output += "0"
        else:
            output += "1"
    return output


if __name__ == '__main__':
    result = find("input.txt")
    print(result[0] * result[1])
