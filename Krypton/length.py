import sys
from collections import Counter

def main():
    with open(sys.argv[1], 'r') as f:
        text = f.read().replace(' ', '').replace('\n', '')


    rep_seq_spaces = []
    for length in range(3, 6):
        substrs = Counter(text[i:i + length] for i in range(len(text) - length + 1))
        for substr, count in substrs.items():
            if count < 2: continue
            first_idx = text.index(substr)
            next_idx = text.index(substr, first_idx + 1)
            rep_seq_spaces.append(next_idx - first_idx)

    tallys = Counter(n % i for n in rep_seq_spaces for i in range(1, 20))
    total = sum(tallys.values())

    if total == 0:
        print("No repeating sequences")
    else:
        print("Chance key length is:")
        for i in range(1, 20):
            print(f"{i} = {round((tallys[i] / total) * 100, 2)}%")

if __name__ == '__main__':
    main()
