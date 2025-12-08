def main():
    with open("day08/08-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    points = []

    for line in data:
        x, y, z = line.split(",")
        points.append((int(x), int(y), int(z)))

    distances = []

    for i in range(len(points)):
        dist_current = []
        for j in range(i + 1, len(points)):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            dist_current.append((j, dist))

        distances.append(dist_current)

    joins = []

    for i in range(1000):
        min_dist = float("inf")
        from_point = -1
        to_point = -1
        index = -1

        for from_point_canc in range(len(distances)):
            for index_cand, (to_point_cand, dist) in enumerate(distances[from_point_canc]):
                if dist < min_dist:
                    min_dist = dist
                    from_point = from_point_canc
                    to_point = to_point_cand
                    index = index_cand

        distances[from_point][index] = (to_point, 9999)

        first_point = -1
        second_point = -1

        for join_index, join in enumerate(joins):
            if from_point in join:
                first_point = join_index
            if to_point in join:
                second_point = join_index

        if first_point == -1 and second_point == -1:
            joins.append([from_point, to_point])

        elif first_point == second_point:
            i -= 1
            continue

        elif first_point == -1 and second_point != -1:
            joins[second_point].append(from_point)

        elif first_point != -1 and second_point == -1:
            joins[first_point].append(to_point)

        else:
            joins[first_point].extend(joins[second_point])
            joins.pop(second_point)

    joins.sort(key=lambda x: len(x), reverse=True)
    print(len(joins[0]) * len(joins[1]) * len(joins[2]))


if __name__ == "__main__":
    main()
