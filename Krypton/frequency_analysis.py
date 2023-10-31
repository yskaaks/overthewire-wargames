#!/usr/bin/python3

import sys
from collections import defaultdict

def main():
    groupsize = int(sys.argv[2])
    char_table = defaultdict(int)

    with open(sys.argv[1]) as file:
        lines = [line.strip().replace(" ", "") for line in file]


    for line in lines:
        for i in range(len(line) - groupsize + 1):
            group = line[i:i+groupsize]
            char_table[group] += 1

    sorted_table = sorted(char_table.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_table:
        print(f"{char}:\t{count}")

if __name__ == "__main__":
    main()
