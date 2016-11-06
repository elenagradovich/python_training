class Bottle:
    def drink(self):
        drink_amount = 175
        if self.water >= drink_amount:
            self.water = self.water - drink_amount
        else:
            self.water = 0

    def show(self):
        print(self.water)

    def __init__(self):
        self.water = 1000

    def __eq__(self, other):
        return self.water == other.water



bottle = Bottle()
bottle2 = Bottle()
print(bottle == bottle2)
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle.drink()
bottle2.drink()
bottle2.drink()
bottle2.drink()
bottle2.drink()
bottle2.drink()
bottle2.drink()
bottle2.drink()

bottle.show()

print(bottle == bottle2)




