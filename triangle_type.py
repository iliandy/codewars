# https://www.codewars.com/kata/53907ac3cd51b69f790006c5/train/python
# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle
# from math import acos, pi
def triangle_type(a, b, c):
    fl_a = float(a)
    fl_b = float(b)
    fl_c = float(c)

    sides = [fl_a, fl_b, fl_c]
    longest = max(sides)
    sides.remove(longest)

    if longest >= sides[0] + sides[1]:
        return 0
    if longest**2 < sides[0]**2 + sides[1]**2:
        return 1
    if longest**2 == sides[0]**2 + sides[1]**2:
        return 2
    if longest**2 > sides[0]**2 + sides[1]**2:
        return 3

    # ang_a = acos((fl_b**2 + fl_c**2 - fl_a**2)/(2*fl_b*fl_c))
    # ang_b = acos((fl_a**2 + fl_c**2 - fl_b**2)/(2*fl_a*fl_c))
    # ang_c = acos((fl_a**2 + fl_b**2 - fl_c**2)/(2*fl_a*fl_b))
    #
    # print "a", ang_a
    # print "b", ang_b
    # print "c", ang_c
    #
    # angs = [ang_a, ang_b, ang_c]
    # if all(ang < pi/2 for ang in angs):
    #     return 1
    # elif ang_a == pi/2 or ang_b == pi/2 or ang_c == pi/2:
    #     return 2
    # elif pi/2 < ang_a < pi or pi/2 < ang_b < pi or pi/2 < ang_c < pi:
    #     return 3
    # else:
    #     return 0

print triangle_type(2, 4, 6)
print triangle_type(8, 5, 7)
print triangle_type(3, 4, 5)
print triangle_type(7, 12, 8)
