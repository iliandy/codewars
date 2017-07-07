# https://www.codewars.com/kata/mumbling/train/python
def accum(s):
    if (s.isalpha()):
        str_lst = []
        for i in range(len(s)):
            str_lst.append(s[i].upper() + (i) * s[i].lower())

        return "-".join(str_lst)
    return "{} contains a non-alpha char".format(s)


s = "abc!"
print accum(s)


# print range(3)
