DIRS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

def main():
    with open("day04/04-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]


    total = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != "@":
                continue
            
            around = 0
            for dx, dy in DIRS:
                around += dir_state(data, x + dx, y + dy)

            if around < 4:
                total += 1

    print(total)


def dir_state(data, x, y):
    if x < 0 or y < 0 or y >= len(data) or x >= len(data[0]):
        return 0
    
    return 1 if data[y][x] == "@" else 0


if __name__ == "__main__":
    main()