def input(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(int(line))
    return lines


def sum(input):
    sums = [];
    for i in range(1, len(input) - 1):
        sums.append(input[i-1] + input[i] + input[i+1])
    return sums


def count():
    numbers = sum(input("Input.txt"))
    result = []

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            result.append('i')
        elif numbers[i] < numbers[i-1]:
            result.append('d')
        else:
            result.append('n')

    return result.count('i')


if __name__ == '__main__':
    print(count())
