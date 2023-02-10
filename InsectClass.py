import random

class Insect:

    def __init__(self, n, l, w):
        self.name = n
        self.legs = l
        self.wings = w
        self.flight = 0

    def length_of_flight(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight

    def get_name(self):
        return self.name
        
        

