class Card:
    def __init__(self, name, cost, power, effect=None):
        self.name = name
        self.cost = cost
        self.power = power
        self.effect = effect

    def __repr__(self):
        return f"{self.name} <{self.cost}> [{self.power}]"
