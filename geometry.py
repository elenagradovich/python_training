from geom2d.point import *


#создаем списки
l1 = [Point(0,3), Point(2,5), Point(1,2)]

#l3 = sorted(l1, key=lambda p: (p.y))
#print(l1)
#print(l3, 'по y')
#l3 = sorted(l1, key=lambda p: (p.x))
#print(l3, 'по x')
# Сортировка по расстояию от центра координат Point(0,0)
l3 = sorted(l1, key=lambda p: p.distance(Point(0,0)))

print(l1)
print(l3)
