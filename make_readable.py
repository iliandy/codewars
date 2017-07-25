# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(sec):
    hh = (sec/60**2) % 100
    mm = (sec/60) % 60
    ss = sec % 60
    return "{:02}:{:02}:{:02}".format(hh, mm, ss)


print make_readable(359999)
