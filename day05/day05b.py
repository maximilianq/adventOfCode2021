def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "Point(x=" + str(self.x) + ", y=" + str(self.y) + ")"


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get(self):
        return self.p1.get(), self.p2.get()

    def diagonal(self):
        return not (self.horizontal() or self.vertical())

    def horizontal(self):
        return self.p1.getY() == self.p2.getY()

    def vertical(self):
        return self.p1.getX() == self.p2.getX()

    def getPoints(self):
        output = []

        left = min(self.p1.getX(), self.p2.getX())
        right = max(self.p1.getX(), self.p2.getX())
        upper = min(self.p1.getY(), self.p2.getY())
        lower = max(self.p1.getY(), self.p2.getY())

        if self.horizontal() and not self.vertical():
            for i in range(left, right + 1):
                output += [i, self.p1.getY()]
        elif self.vertical() and not self.horizontal():
            for i in range(upper, lower + 1):
                output += [self.p1.getX(), i]
        else:
            if (self.p1.getX() == left and self.p1.getY() == upper) or (self.p2.getX() == left and self.p2.getY() == upper):
                for i in range(0, (lower + 1) - upper):
                    output += [left + i, upper + i]
            else:
                for i in range(0, (lower + 1) - upper):
                    output += [left + i, lower - i]

        return output

    def __str__(self):
        return "Line(p1=" + str(self.p1) + ", p2=" + str(self.p2) + ")"


def convert(path):
    _lines = input(path)
    output = []

    for _line in _lines:
        _p1 = _line.split(" -> ")[0]
        _p2 = _line.split(" -> ")[1]
        p1 = Point(int(_p1.split(",")[0]), int(_p1.split(",")[1]))
        p2 = Point(int(_p2.split(",")[0]), int(_p2.split(",")[1]))
        output.append(Line(p1, p2))

    return output


def process(path):
    data = convert(path)
    dictionary = {}

    for dataElement in data:
        _points = dataElement.getPoints()
        for i in range(0, int(len(_points) / 2)):
            key = str(_points[2*i]) + "_" + str(_points[(2*i) + 1])
            if key in dictionary:
                dictionary[key] = dictionary[key] + 1
            else:
                dictionary[key] = 1

    counter = 0
    for key in dictionary.keys():
        if dictionary[key] >= 2:
            counter += 1

    print(counter)


if __name__ == '__main__':
    process("input.txt")
