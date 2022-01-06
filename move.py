class Move:
    def __init__(self, name: str, description: str, power: int, action_type: str, effect_type: str, type: str, maxPP):
        self.name = name
        self.description = description
        self.power = power
        self.action_type = action_type # physical or special
        self.effect_type = effect_type # attack, status, buff or debuff
        self.type = type
        self.maxPP = maxPP
        self.currentPP = maxPP

    def decrementPP (self) -> bool:
        if (self.currentPP > 0):
            self.currentPP -= 1
            return True
        else:
            return False
        