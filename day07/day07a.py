def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(path):
    lines = input(path)[0].split(",")

    temp = []
    for line in lines:
        temp.append(int(line))

    output = {}
    for tempElement in temp:
        if tempElement in output:
            output[tempElement] += 1
        else:
            output[tempElement] = 1

    return output

def fuel(data, position):
    output = 0
    for dataElement in data.keys():
        output += abs(dataElement - position) * data[dataElement]
    return output


def process(path):
    data = convert(path)

    minimum = fuel(data, min(data.keys()))

    for i in range(min(data.keys()) + 1, max(data.keys())):
        actual = fuel(data, i)
        if actual < minimum:
            minimum = actual

    return minimum


if __name__ == '__main__':
    print(process("input.txt"))
