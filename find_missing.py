# https://www.codewars.com/kata/find-the-missing-term-in-an-arithmetic-progression/train/python

def find_missing(seq):
    step = (seq[-1] - seq[0])/len(seq)
    comp_seq = range(seq[0], seq[-1], step)
    if (set(comp_seq) - set(seq)):
        return (set(comp_seq) - set(seq)).pop()

print find_missing([1, 2, 3, 4, 6, 7, 8, 9])
