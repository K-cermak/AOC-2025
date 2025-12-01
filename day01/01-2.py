def main():
    with open("day01/01-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    curr = 50
    zeros = 0

    for line in data:
        if line[0] == "L":
            if curr == 0:
                zeros -= 1

            curr -= int(line[1:])
            zeros -= curr // 100

            if curr % 100 == 0:
                zeros += 1

        elif line[0] == "R":
            curr += int(line[1:])
            zeros += curr // 100

        curr %= 100

    print(zeros)


if __name__ == "__main__":
    main()
