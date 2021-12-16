def read(_path):
    lines = []
    with open(_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(_path):
    output = []
    line = read(_path)[0]
    for character in list(bin(int(line, 16))[2:].zfill(len(line) * 4)):
        output.append(int(character))
    return output


def toDecimal(_data, _filtered):
    output = 0
    for i in range(len(_data)):
        if (not _filtered and (i % 5) != 0) or _filtered:
            output = (output << 1) | _data[i]
    return output


def getLength(_data, _start):

    if toDecimal(_data[_start + 3:_start + 6], True) == 4:
        count = 0
        while _data[_start + 6 + (count * 5)] == 1:
            count += 1
        _length = (count + 1) * 5
        return _length + 6

    else:
        if _start + 6 > len(_data):
            return - 1
        if _data[_start + 6] == 0:
            return toDecimal(_data[_start + 7:_start + 22], True) + 22
        else:
            count = toDecimal(_data[_start + 7:_start + 18], True)
            _count = 0
            _length = 18
            while _count < count:
                _count += 1
                _length += getLength(_data, _start + _length)
            return _length


def getSubPackets(_data, _start):

    if _data[_start + 6] == 0:
        size = toDecimal(_data[_start + 7:_start + 22], True)
        length = 0
        start = _start + 22
        count = 0
        result = []
        while start <= (size + 22):
            _length = getLength(_data, start)
            if _length == -1:
                break
            length += _length
            result.append(_data[start:start+_length])
            start = start + _length
            count += 1
        return result
    else:

        [count, _count] = [toDecimal(_data[_start + 7:_start + 18], True), 0]
        length = 0
        start = _start + 18
        result = []
        while _count < count:
            _length = getLength(_data, start)
            length += _length
            result.append(_data[start:start+_length])
            start = start + _length
            _count += 1
        return result


class Packet:

    def __init__(self, _data):

        if toDecimal(_data[3:6], True) == 4:

            self.version = toDecimal(_data[0:3], True)

            self.type = toDecimal(_data[3:6], True)

            self.value = toDecimal(_data[6:len(_data)], False)

        else:

            self.version = toDecimal(_data[0:3], True)

            self.type = toDecimal(_data[3:6], True)

            self.subPackets = []

            for subPacket in getSubPackets(_data, 0):
                self.subPackets.append(Packet(subPacket))

    def sum(self):
        if self.type == 4:
            return self.version

        return sum([subPacket.sum() for subPacket in self.subPackets]) + self.version

    def evaluate(self):

        if self.type == 0:
            return sum([subPacket.evaluate() for subPacket in self.subPackets])

        elif self.type == 1:
            output = 1
            for subPacket in self.subPackets:
                output *= subPacket.evaluate()
            return output

        elif self.type == 2:
            return min([subPacket.evaluate() for subPacket in self.subPackets])

        elif self.type == 3:
            return max([subPacket.evaluate() for subPacket in self.subPackets])

        elif self.type == 4:
            return self.value

        elif self.type == 5:
            return int(self.subPackets[0].evaluate() > self.subPackets[1].evaluate())

        elif self.type == 6:
            return int(self.subPackets[0].evaluate() < self.subPackets[1].evaluate())

        elif self.type == 7:
            return int(self.subPackets[0].evaluate() == self.subPackets[1].evaluate())


def partA(_path):
    data = convert(_path)
    packet = Packet(data[0:getLength(data, 0)])
    return packet.sum()


def partB(_path):
    data = convert(_path)
    packet = Packet(data[0:getLength(data, 0)])
    return packet.evaluate()


if __name__ == '__main__':
    print(partA("input.txt"))
    print(partB("input.txt"))
