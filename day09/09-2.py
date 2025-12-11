import math


def main():
    with open("day09/09-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    points = []

    for line in data:
        (
            x,
            y,
        ) = line.split(",")
        points.append((int(x), int(y)))

    is_x = False
    len_ = len(points)
    for i in range(len_):
        p1 = points[i]
        p2 = points[(i + 1) % len_]

        if is_x:
            x_start = min(p1[0], p2[0])
            x_end = max(p1[0], p2[0])
            for x in range(x_start, x_end + 1):
                points.append((x, p1[1]))

        else:
            y_start = min(p1[1], p2[1])
            y_end = max(p1[1], p2[1])
            for y in range(y_start, y_end + 1):
                points.append((p1[0], y))

        is_x = not is_x

    points_set = set(points)

    values = []
    for i in range(len_):
        for j in range(i, len_):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]

            size = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            values.append((size, x1, y1, x2, y2))

    values.sort()

    # get max_x, min_x, max_y, min_y

    max_x = float("-inf")
    min_x = float("inf")
    max_y = float("-inf")
    min_y = float("inf")

    for point in points:
        x = point[0]
        y = point[1]

        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    max_ = 0
    while True:
        print(len(values))
        size, x1, y1, x2, y2 = values.pop()
        is_inside = True

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if not is_inside_check(x, y, points_set, min_x, max_x, min_y, max_y):
                    is_inside = False
                    break
            if not is_inside:
                break

        if is_inside:
            max_ = size
            break

    print(max_)


def is_inside_check(x, y, points, min_x, max_x, min_y, max_y):
    if (x, y) in points:
        return True

    y_current = y
    while True:
        y_current -= 1
        if (x, y_current) in points:
            break
        if y_current < min_y - 1:
            return False

    y_current = y
    while True:
        y_current += 1
        if (x, y_current) in points:
            break
        if y_current > max_y + 1:
            return False

    x_current = x
    while True:
        x_current -= 1
        if (x_current, y) in points:
            break
        if x_current < min_x - 1:
            return False

    x_current = x
    while True:
        x_current += 1
        if (x_current, y) in points:
            break
        if x_current > max_x + 1:
            return False

    return True


def print_points(points):
    min_x = 0
    max_x = float("-inf")
    min_y = 0
    max_y = float("-inf")

    for point in points:
        x = point[0]
        y = point[1]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    for y in range(int(min_y), int(max_y) + 1):
        line = ""
        for x in range(int(min_x), int(max_x) + 1):
            if (x, y) in points:
                line += "#"
            else:
                line += "."
        print(line)


if __name__ == "__main__":
    main()
