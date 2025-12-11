def main():
    with open("day10/10-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0

    for line in data:
        parts = line.split(" ")
        target = parts[-1]
        options = parts[1:-1]

        target_int = []
        target = target[1:-1]
        target_parts = target.split(",")
        for i in range(len(target_parts)):
            target_int.append(int(target_parts[i]))

        options_parse = []
        for i in range(len(options)):
            option = options[i][1:-1]
            option_parts = option.split(",")
            option_parts_int = []
            for j in range(len(option_parts)):
                option_parts_int.append(int(option_parts[j]))
            options_parse.append(option_parts_int)

        res = rec_check(target_int, [0] * len(target_int), options_parse, 0, 0)
        if res is None:
            assert False, "No solution found"
        print(res)
        count += res

    print(count)


def rec_check(want, current, rules, index, depth):
    if want == current:
        return depth

    if index >= len(rules):
        return None

    res1 = rec_check(want, current, rules, index + 1, depth)

    res2 = None
    new = current.copy()

    while True:
        correct = True

        for i, value in enumerate(new):
            if value > want[i]:
                correct = False
                break
        
        if not correct:
            break

        for option in rules[index]:
            new[option] += 1

        depth += 1
        res_cand = rec_check(want, new, rules, index + 1, depth)
        if res_cand is not None:
            if res2 is None or res_cand < res2:
                res2 = res_cand

    if res1 is None:
        return res2
    if res2 is None:
        return res1
    return min(res1, res2)


if __name__ == "__main__":
    main()
