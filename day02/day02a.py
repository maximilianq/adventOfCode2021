def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(data):
    operations = []
    values = []
    for line in data:
        content = line.split()
        operations.append(content[0])
        values.append(int(content[1]))
    return operations, values


def calculate(path):
    lines = input(path)
    converted = convert(lines)
    operations = converted[0]
    values = converted[1]

    x = 0
    y = 0

    for i in range(len(operations)):
        if operations[i] == "forward":
            x += values[i]
        elif operations[i] == "up":
            y -= values[i]
        else:
            y += values[i]
    return x, y


if __name__ == '__main__':
    result = calculate("input.txt")
    print(result[0] * result[1])
