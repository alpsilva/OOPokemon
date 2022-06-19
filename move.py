import json

from sklearn.cluster import DBSCAN

class Move:
    def __init__(self, name: str, description: str, power: int, action_type: str, effect_type: str, type: str, maxPP: int):
        self.name = name
        self.description = description
        self.power = power
        self.action_type = action_type # physical or special
        self.effect_type = effect_type # attack, status, buff or debuff
        self.type = type
        self.maxPP = maxPP
        self.currentPP = maxPP

    def __iter__(self):
        yield 'name', self.name
        yield 'description', self.description
        yield 'power', self.power
        yield 'action_type', self.action_type
        yield 'effect_type', self.effect_type
        yield 'type', self.type
        yield 'maxPP', self.maxPP
        yield 'currentPP', self.currentPP

    def decrementPP (self) -> bool:
        if (self.currentPP > 0):
            self.currentPP -= 1
            return True
        return False