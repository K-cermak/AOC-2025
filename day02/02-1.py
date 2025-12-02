def main():
    with open("day02/02-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    invalid_count = 0

    data = data[0].split(",")
    for seq in data:
        seq = seq.split("-")
        start = int(seq[0])
        end = int(seq[1])

        for num in range(start, end + 1):
            digits = [int(d) for d in str(num)]

            if len(digits) % 2 != 0:
                continue

            is_ok = True

            for j in range(0, len(digits) // 2):
                if digits[j] != digits[j + (len(digits) // 2)]:
                    is_ok = False
                    break

            if is_ok:
                invalid_count += num

    print(invalid_count)


if __name__ == "__main__":
    main()
