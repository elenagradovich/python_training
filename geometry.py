from geom2d.point import *


#создаем списки
l1 = [Point(0,0), Point(2,5), Point(8,3)]
#l2 = [Point(0,0), Point(2,5), Point(8,3)]
l2 = list(l1)
l2[0] = Point(0,0)

print(l1 == l2)

