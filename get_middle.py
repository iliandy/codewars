# https://www.codewars.com/kata/get-the-middle-character/train/python
def get_middle(s):
    if (len(s) % 2 == 1):
        return s[len(s)/2]
    if (len(s) % 2 == 0):
        return s[len(s)/2 - 1] + s[len(s)/2]

s = "middle"
print get_middle(s)
