def main():
    with open("day10/10-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    count = 0

    for line in data:
        parts = line.split(" ")
        target = parts[0]
        options = parts[1:-1]

        target_bool = []
        for target_char in target:
            if target_char == ".":
                target_bool.append(False)
            elif target_char == "#":
                target_bool.append(True)

        options_parse = []
        for i in range(len(options)):
            option = options[i][1:-1]
            option_parts = option.split(",")
            option_parts_int = []
            for j in range(len(option_parts)):
                option_parts_int.append(int(option_parts[j]))
            options_parse.append(option_parts_int)

        res = rec_check(target_bool, [False] * len(target_bool), options_parse, 0, 0)
        if res is None:
            assert False, "No solution found"
        count += res

    print(count)


def rec_check(want, current, rules, index, depth):
    if want == current:
        return depth

    if index >= len(rules):
        return None

    res1 = rec_check(want, current, rules, index + 1, depth)

    new = current.copy()
    for option in rules[index]:
        new[option] = not new[option]
    res2 = rec_check(want, new, rules, index + 1, depth + 1)

    if res1 is None:
        return res2
    if res2 is None:
        return res1
    return min(res1, res2)


if __name__ == "__main__":
    main()
