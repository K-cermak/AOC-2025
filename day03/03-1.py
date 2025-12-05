def main():
    with open("day03/03-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    comb_sum = 0

    for line in data:
        max_combination = 0

        for i, char_i in enumerate(line):
            for j, char_j in enumerate(line):
                if i >= j:
                    continue

                comb = int(char_i) * 10 + int(char_j)
                if comb > max_combination:
                    max_combination = comb

        comb_sum += max_combination

    print(comb_sum)



if __name__ == "__main__":
    main()