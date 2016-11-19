from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    #Сравнение
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    #Сортировка по возрастанию
    def __lt__(self, other):
        return self.y < other.y

    #Вывод в удобной форме
    def __repr__(self):
        return "Point (%s, %s)"%(self.x, self.y)