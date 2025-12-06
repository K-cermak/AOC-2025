def main():
    with open("day06/06-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    nums = []
    ops = []

    for index, line in enumerate(data):
        while "  " in line:
            line = line.replace("  ", " ")

        parts = line.split(" ")
        parts = [part for part in parts if part != ""]

        for subindex, part in enumerate(parts):
            if index != len(data) - 1:
                if subindex >= len(nums):
                    nums.append([int(part)])
                else:
                    nums[subindex].append(int(part))

            else:
                ops.append(part)

    sum_ = 0

    for index, op in enumerate(ops):
        if op == "+":
            count = 0
            for num_list in nums[index]:
                count += num_list
            sum_ += count

        elif op == "*":
            prod = 1
            for num_list in nums[index]:
                prod *= num_list
            sum_ += prod

    print(sum_)


if __name__ == "__main__":
    main()
