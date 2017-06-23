def likes(names):
    names_2 = names[:2]
    names_rest = names[2:]

    if (len(names) == 0):
        names_str = "no one"
    elif (len(names) == 1 or len(names) == 2):
        names_str = " and ".join(names)
    elif (len(names) == 3):
        names_str = " and ".join([", ".join(names_2)] + names_rest)
    elif (len(names) >= 4):
        other_names_num = len(names) - 2
        names_str = " and ".join([", ".join(names_2)] + ["{} others".format(other_names_num)])

    if (0 <= len(names) <= 1):
        return "{} likes this".format(names_str)
    else:
        return "{} like this".format(names_str)

print likes(names)
