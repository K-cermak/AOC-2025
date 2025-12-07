from functools import cache

data = []


def main():
    global data
    with open("day07/07-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    beam = 0
    for index, item in enumerate(data[0]):
        if item == "S":
            beam = index
            break

    print(rec_calc(0, beam))


@cache
def rec_calc(level, beam):
    if level >= len(data):
        return 1

    while data[level][beam] == ".":
        level += 1
        if level >= len(data):
            return 1

    count = 0
    count += rec_calc(level + 1, beam - 1)
    count += rec_calc(level + 1, beam + 1)

    return count


if __name__ == "__main__":
    main()
