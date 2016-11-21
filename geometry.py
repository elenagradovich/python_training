from geom2d.point import *


#создаем списки
#l1 = [Point(0,3), Point(2,5), Point(1,2)]

#l3 = sorted(l1, key=lambda p: (p.y))
#print(l1)
#print(l3, 'по y')
#l3 = sorted(l1, key=lambda p: (p.x))
#print(l3, 'по x')
# Сортировка по расстояию от центра координат Point(0,0)
#l3 = sorted(l1, key=lambda p: p.distance(Point(0,0)))
#print(l1)
#print(l3)
#l = [Point(i, i*i) for i in range (-5, 6)]
#l2 = [Point(el.x, -el.y) for el in l]
#l2 = list(map(lambda p: Point(p.x, -p.y), l))
#l2 = list(filter(lambda p: p.x>0, l)) #фильтр на положительные координаты
l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
l2 = list(filter(lambda p: p.x%2 == 0, l)) #четные координаты


print (l)
print (l2)