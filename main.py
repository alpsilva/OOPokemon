from move import Move
from pokemon import Pokemon

p1 = Pokemon("Bulbasaur", "Bulbo", 1, "grass", "poison")

m1 = Move("Tackle", "", 40, "physical", "attack", "normal", 40)

p1.set_move(0, m1)

print(p1)