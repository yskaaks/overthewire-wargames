#!/bin/usr/python3
import sys

def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = sys.argv[2]

    with open(sys.argv[1], 'r') as f:
        text = f.read().replace(' ', '').replace('\n', '')

    decode = lambda c, k: alphabet[(alphabet.index(c) - alphabet.index(k)) % 26]
    s = ''.join(decode(text[i], key[i % len(key)]) for i in range(len(text)))

    print(s)

if __name__ == '__main__':
    main()
