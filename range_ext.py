# https://www.codewars.com/kata/range-extraction/train/python
def range_ext(lst):
    new_lst = []
    start = end = lst[0]

    for n in lst[1:] + [""]:
        if n != end + 1:
            if end == start:
                new_lst.append(str(start))
            elif end == start + 1:
                new_lst.extend([str(start), str(end)])
            else:
                new_lst.append(str(start) + "-" + str(end))
            start = n
        end = n

    return ",".join(new_lst)


print range_ext([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
