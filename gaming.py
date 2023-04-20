from PIL import Image
import random


class Player:
    def __init__(self,HP,Weapon,Name):
        self.HP = HP
        self.Weapon = Weapon
        self.Name = Name
        
    def parry(self):
        parry1 = [1,2]
        chance = random.choice(parry1)
        if chance == 2:
            print('You parried')
        else:
            print('You got hit...')
            self.HP - 50
            
  

Ly = Player(100,"Sword","Lie Lee")

Ly.parry()
print(Ly.HP)
    

    


