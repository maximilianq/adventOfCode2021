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
        [_history, _actual] = line.split(" | ")
        output.append(Pattern(_history.split(" "), _actual.split(" ")))
    return output


class Pattern:

    def __init__(self, _history, _actual):
        self.history = _history
        self.actual = _actual
        self.dictionary = self.decrypt()


    def characterA(self, _index):
        length = len(self.actual[_index])
        if length == 2:
            return [1]
        elif length == 4:
            return [4]
        elif length == 3:
            return [7]
        elif length == 7:
            return [8]
        else:
            return [0, 2, 3, 5, 6, 9]

    def characterB(self, _index):
        for key in self.dictionary:
            if self.dictionary[key] == "".join(sorted(self.actual[_index])):
                return key

    def decrypt(self):
        dictionary = {1: self.filter(2)[0], 4: self.filter(4)[0], 7: self.filter(3)[0], 8: self.filter(7)[0]}

        _five = self.filter(5)
        _six = self.filter(6)

        _indexThree = findThree(_five)
        dictionary[3] = _five[_indexThree]

        _indexFive = findFive(_five, _indexThree, dictionary[4])
        dictionary[5] = _five[_indexFive]

        dictionary[2] = _five[3 - _indexThree - _indexFive]

        _indexSix = findSix(_six, dictionary[1])
        dictionary[6] = _six[_indexSix]

        _indexZero = findZero(_six, _indexSix, dictionary[4])
        dictionary[0] = _six[_indexZero]

        dictionary[9] = _six[3 - _indexSix - _indexZero]

        for key in dictionary:
            dictionary[key] = "".join(sorted(dictionary[key]))

        return dictionary

    def filter(self, _count):
        output = []
        for historyElement in self.history:
            if len(historyElement) == _count:
                output.append(historyElement)
        return output


def difference(_x, _y):
    output = ""
    for i in range(len(_x)):
        if not _x[i] in _y:
            output += _x[i]
    return output


def findZero(_data, _six, _four):
    for i in range(0, 3):
        if i != _six:
            diff = difference(_four, _data[i])
            if len(diff) != 0:
                return i
    return 0


def findThree(_data):
    for i in range(0, 3):
        for j in range(0, 3):
            if not i == j:
                diff = difference(difference(_data[i], _data[j]), _data[3 - i - j]);
                if diff == "":
                    return i
    return 0


def findFive(_data, _three, _four):
    for i in range(0, 3):
        if i != _three:
            diff = difference(_data[i], _four)
            if len(diff) == 2:
                return i
    return 0


def findSix(_data, _one):
    for i in range(0, 3):
        diff = difference(_one, _data[i])
        if len(diff) != 0:
            return i
    return 0


def partA(_path):
    data = convert(_path)
    count = 0
    for dataElement in data:
        for i in range(0, 4):
            if len(dataElement.characterA(i)) == 1:
                count += 1
    return count


def partB(_path):
    data = convert(_path)
    result = 0;
    for dataElement in data:
        value = 0
        for i in range(0, 4):
            value += pow(10, 3-i) * dataElement.characterB(i)
        result += value
    return result


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
