# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(string):
    wrd_lst = string.split(" ")
    wgt_lst = [sum(map(int, list(wrd))) for wrd in wrd_lst]
    tup_lst = zip(wrd_lst, wgt_lst)
    srted_tups = sorted(tup_lst, key=lambda tup: (tup[1], tup[0]))
    return str(" ".join([tup[0] for tup in srted_tups]))


print order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
