def range_ext(lst):
    new_lst = []
    start = end = lst[0]

    for n in lst[1:] + [""]:
        if n != end + 1:
            if end == start:
                new_lst.append( str(start) )
            elif end == start + 1:
                new_lst.extend( [str(start), str(end)] )
            else:
                new_lst.append( str(start) + "-" + str(end) )
            start = n
        end = n

    return ",".join(new_lst)


    # count = 0
    # new_arr = []
    # for i in range(len(arr) - 1):
    #     ind = i
    #     if arr[i] + 1 == arr[i+1]:
    #         count += 1
    #     else:
    #         if count == 1:
    #             new_arr.append(str(arr[i - 1]))
    #             new_arr.append(str(arr[i]))
    #             count = 0
    #         elif count >= 2:
    #             new_arr.append("{}-{}".format(str(arr[i - count]), str(arr[i])))
    #             count = 0
    #         else:
    #             new_arr.append(str(arr[i]))
    #
    # ind += 1
    # if count == 1:
    #     new_arr.append(str(arr[ind - 1]))
    #     new_arr.append(str(arr[ind]))
    #     count = 0
    # elif count >= 2:
    #     new_arr.append("{}-{}".format(str(arr[ind - count]), str(arr[ind])))
    #     count = 0
    # else:
    #     new_arr.append(str(arr[ind]))
    #
    # return ",".join(new_arr)

print range_ext([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
