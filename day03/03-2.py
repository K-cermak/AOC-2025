def main():
    with open("day03/03-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    comb_sum = 0

    for line in data:
        max_combination = 0

        res = []
        get_comb(line, 0, [], res)

        for subres in res:
            sum_ = 0
            for n in subres:
                sum_ = sum_ * 10 + n

            if sum_ > max_combination:
                max_combination = sum_

        comb_sum += max_combination

    print(comb_sum)


def get_comb(line: str, index: int, inserted: list[int], res: list[list[int]]):
    for subres in res:
        for i, char in enumerate(inserted):
            if char < subres[i]:
                return

    if len(inserted) == 12:
        if inserted not in res:
            res.append(inserted.copy())

        return

    if index >= len(line):
        return

    get_comb(line, index + 1, inserted, res)
    get_comb(line, index + 1, inserted + [int(line[index])], res)


if __name__ == "__main__":
    main()
