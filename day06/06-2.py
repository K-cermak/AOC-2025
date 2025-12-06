def main():
    with open("day06/06-input.txt", "r") as file:
        data = file.readlines()
        data = [line.replace("\n", "") for line in data]

    ops = []

    for part in data[-1].split(" "):
        if not part:
            continue

        ops.append(part)

    spaces = []

    for i in range(len(data[0])):
        is_space = True

        for j in range(len(data)):
            if data[j][i] != " ":
                is_space = False
                break

        if is_space:
            spaces.append(i)

    new_data = []

    for i in range(len(data) - 1):
        line = data[i]
        result = []
        prev = 0
        for idx in spaces:
            result.append(line[prev:idx])
            prev = idx
        result.append(line[prev:])
        new_data.append(result)

    total_sum = 0

    for i in range(len(new_data[0])):
        longest_num = 0
        for j in range(len(new_data)):
            if len(new_data[j][i]) > longest_num:
                longest_num = len(new_data[j][i])

        if i == 0:
            longest_num += 1

        nums = []
        for j in range(-1, -longest_num, -1):
            curr_num = 0
            for k in range(len(new_data)):
                item = new_data[k][i][j]
                if item != " " and item != "":
                    curr_num *= 10
                    curr_num += int(item)
            nums.append(curr_num)

        if ops[i] == "+":
            count = 0
            for num in nums:
                count += num
            total_sum += count

        elif ops[i] == "*":
            prod = 1
            for num in nums:
                prod *= num
            total_sum += prod

    print(total_sum)


if __name__ == "__main__":
    main()
