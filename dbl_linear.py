# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python
def dbl_linear(n):
    nums = [1]
    for num in nums:
        nums.extend([2 * num + 1, 3 * num + 1])
        if len(nums) > 9 * n:
            break

    return sorted(set(nums))[n]

print dbl_linear(50)
