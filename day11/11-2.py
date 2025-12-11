import sys
from functools import cache

inputs = {}


def main():
    with open("day11/11-input.txt", "r") as file:
        data = file.readlines()
        data = [line.rstrip() for line in data]

    for line in data:
        parts = line.split(": ")
        key = parts[0]
        values = parts[1].split(" ")
        inputs[key] = values

    sum_ = find("svr", False, False)
    print(sum_)


@cache
def find(current, dac_found, fft_found):
    if current == "out":
        if dac_found and fft_found:
            return 1

        return 0

    total = 0
    for next_ in inputs[current]:
        total += find(
            next_,
            dac_found or next_ == "dac",
            fft_found or next_ == "fft",
        )
    return total


if __name__ == "__main__":
    main()
