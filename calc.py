class Arthemetic():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x // self.y

#######example#########
a = Arthemetic(2,4)
print(a.add())  #6
print(a.multiply()) #8
print(a.subtract()) #-2
print(a.divide()) #0
