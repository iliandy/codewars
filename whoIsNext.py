# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python
# Couldn't get it to work correctly with large int
def whoIsNext(names, rnds):
    for rnd in xrange(rnds):
        next = names.pop(0)
        names += [next, next]
    return next

    # solution:
    # while r > 5:
    #     r = (r - 4) / 2
    # return names[r-1]

print whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52)
