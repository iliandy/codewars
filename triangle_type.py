# https://www.codewars.com/kata/53907ac3cd51b69f790006c5/train/python
# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle
def triangle_type(a, b, c):
    import math
    fl_a = float(a)
    fl_b = float(b)
    fl_c = float(c)
    ang_a = math.acos((fl_b**2 + fl_c**2 - fl_a**2)/(2*fl_b*fl_c))
    ang_b = math.acos((fl_a**2 + fl_c**2 - fl_b**2)/(2*fl_a*fl_c))
    ang_c = math.acos((fl_a**2 + fl_b**2 - fl_c**2)/(2*fl_a*fl_b))

    print "a", ang_a
    print "b", ang_b
    print "c", ang_c

    angs = [ang_a, ang_b, ang_c]
    if all(ang < math.pi/2 for ang in angs):
        return 1
    elif ang_a == math.pi/2 or ang_b == math.pi/2 or ang_c == math.pi/2:
        return 2
    elif math.pi/2 < ang_a < math.pi or math.pi/2 < ang_b < math.pi or math.pi/2 < ang_c < math.pi:
        return 3
    else:
        return 0

print triangle_type(2, 4, 6)
print triangle_type(8, 5, 7)
print triangle_type(3, 4, 5)
print triangle_type(7, 12, 8)
