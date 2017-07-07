def narcissistic(num):
    int_str = str(num)
    exp = len(int_str)

    sum = 0
    for digit in int_str:
        sum += int(digit)**exp

    if sum == num:
        return True

    return False

print narcissistic(153)
print narcissistic(1634)
print narcissistic(122)
