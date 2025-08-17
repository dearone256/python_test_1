from geom2d.point import *

# a = Point (0, 0)
# b = Point (3, 4)
# print (a.distance (b))
# print (a == b)
# print (a == Point (0, 0))

l1 = [Point(0,0), Point(1,2), Point(2,1)]
l2 = [Point(0,0), Point(1,2), Point(2,1)]
print(l1 == l2)

l1 = [Point(0,0), Point(1,2), Point(2,1)]
l2 = l1
print(l1 == l2)

l1 = [Point(0,0), Point(1,2), Point(2,1)]
l2 = list(l1)
print(l1 == l2)

l1 = [Point(0,0), Point(1,2), Point(2,1)]
l2 = list(l1)
l2[0] = Point(0,0)
print(l1 == l2)