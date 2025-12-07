def main():
    with open("day07/07-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    current = set()
    for index, item in enumerate(data[0]):
        if item == "S":
            current.add(index)
            break

    hits = 0

    for i in range(1, len(data)):
        line = data[i]
        new_curr = set()
        for item in current:
            if line[item] == ".":
                new_curr.add(item)
            elif line[item] == "^":
                hits += 1
                new_curr.add(item - 1)
                new_curr.add(item + 1)

        current = new_curr

    print(hits)

if __name__ == "__main__":
    main()