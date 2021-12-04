def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def toIntArray(input):
    output = []
    for inputElement in input:
        output.append(int(inputElement))
    return output


def convert(path):
    lines = input(path)
    numbers = toIntArray(lines[0].split(","))
    games = []
    temp = []
    for i in range(2, len(lines)):
        print(lines[i])
        if (i - 1) % 6 == 0:
            games.append(Bingo(temp))
            temp = []
        else:
            temp = temp + toIntArray(lines[i].strip().replace("  ", " ").split(" "))
    return games, numbers


class Bingo:

    def __init__(self, data):
        self.data = data

    def check(self, numbers):
        return self.checkRows(numbers) or self.checkColumns(numbers)

    def checkRows(self, numbers):
        for i in range(0, 5):
            found = True
            for j in range(0, 5):
                if not self.data[(i * 5) + j] in numbers:
                    found = False
                    break
            if found:
                return True
        return False

    def checkColumns(self, numbers):
        for i in range(0, 5):
            found = True
            for j in range(0, 5):
                if not self.data[(j * 5) + i] in numbers:
                    found = False
                    break
            if found:
                return True
        return False

    def sum(self, numbers):
        output = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if not self.data[(i * 5) + j] in numbers:
                    output += self.data[(i * 5) + j]
        return output


def check(games, numbers):
    checking = []
    for i in range(0, len(numbers)):
        checking.append(numbers[i])
        won = []
        for game in games:
            if game.check(checking):
                won.append(game)
                games.remove(game)
        if len(won) > 0 and len(games) == 0:
            return won[0].sum(checking), numbers[i]
    return 0, 0


if __name__ == '__main__':
    result = convert("input.txt")
    example = check(result[0], result[1])
    print(example[0] * example[1])
    print(example[1])
