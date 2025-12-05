def main():
    with open("day05/05-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    items = []

    for line in data:
        if line == "":
            break

        parts = line.split("-")
        start = int(parts[0])
        end = int(parts[1])
        items.append((start, end))

    items.sort()
    merged_items = []
    current_start, current_end = items[0]

    for start, end in items[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged_items.append((current_start, current_end))
            current_start, current_end = start, end

    merged_items.append((current_start, current_end))

    count = 0
    for start, end in merged_items:
        count += end - start + 1

    print(count)


if __name__ == "__main__":
    main()
