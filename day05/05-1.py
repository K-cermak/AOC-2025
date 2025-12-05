def main():
    with open("day05/05-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    ok_ranges = []
    count = 0
    ranges = True

    for line in data:
        if line == "":
            ranges = False
            continue

        if ranges:
            parts = line.split("-")
            start = int(parts[0])
            end = int(parts[1])
            ok_ranges.append((start, end))

        else:
            number = int(line)
            for r in ok_ranges:
                low, high = r
                if low <= number <= high:
                    count += 1
                    break

    print(count)


if __name__ == "__main__":
    main()