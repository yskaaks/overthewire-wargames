#!/usr/bin/python3

import sys

def main():
    key_length = int(sys.argv[2])
    shift = int(sys.argv[3]) if len(sys.argv) == 4 else 0

    with open(sys.argv[1]) as file:
        lines = [line.strip().replace(" ", "") for line in file]

    out_string = ""

    for line in lines:
        line = line[shift::key_length]
        out_string += line

    print(out_string)

if __name__ == "__main__":
    main()
