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

            if len(digits) < 2:
                continue

            for seq_len in range(1, len(digits) // 2 + 1):
                if len(digits) % seq_len != 0:
                    continue

                has_seq = True

                for i in range(len(digits) // seq_len): # outer sequence
                    for j in range(seq_len): # in sequence
                        if digits[j] != digits[i * seq_len + j]:
                            has_seq = False
                            break

                if has_seq:
                    invalid_count += num
                    break


    print(invalid_count)


if __name__ == "__main__":
    main()
