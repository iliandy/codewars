# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python
# NOT PASSING ALL TESTS!!!!!!!!!!!!!
def goodVsEvil(good, evil):
    good_sum = 0
    evil_sum = 0
    good_vals = [1, 2, 3, 3, 4, 10]
    evil_vals = [1, 2, 2, 2, 3, 5, 10]

    good_nums = [int(good[i]) for i in range(0, len(good), 2) if good[i].isdigit()]
    evil_nums = [int(evil[i]) for i in range(0, len(evil), 2) if evil[i].isdigit()]

    good_sum = sum([num * val for num, val in zip(good_nums, good_vals)])
    evil_sum = sum([num * val for num, val in zip(evil_nums, evil_vals)])

    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    elif good_sum < evil_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
print goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0')
print goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0')
