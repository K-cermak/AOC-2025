def main():
    with open("day11/11-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    inputs = {}

    for line in data:
        parts = line.split(": ")
        key = parts[0]
        values = parts[1].split(" ")
        inputs[key] = values

    sum_ = find(inputs, "you")
    print(sum_)


def find(inputs, current):
    if current == "out":
        return 1

    total = 0
    for next_ in inputs[current]:
        total += find(inputs, next_)

    return total


if __name__ == "__main__":
    main()
