def main():
    with open("day09/09-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    points = []

    for line in data:
        x, y, = line.split(",")
        points.append((x, y))

    max_ = 0

    for i in range(len(points)):
        for j in range(i, len(points)):
            x1 = int(points[i][0])
            y1 = int(points[i][1])
            x2 = int(points[j][0])
            y2 = int(points[j][1])

            size = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if size > max_:
                max_ = size

    print(max_)

if __name__ == "__main__":
    main()