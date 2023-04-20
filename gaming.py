from PIL import Image
import random


class Player:
    def __init__(self,HP,Weapon,Name,Damage,remaining_HP):
        self.HP = HP
        self.Weapon = Weapon
        self.Name = Name
        self.Damage = Damage
        self.remaining_HP = remaining_HP
        
    def parry(self):
        parry1 = [1,2]
        chance = random.choice(parry1)
        if chance == 2:
            print('You parried')
        else:
            print('You missed the parry')
            self.damage()


  
        
        return chance
    def damage(self):
        chance = self.parry()
        if chance != 2:
            self.remaining_HP = self.HP - self.Damage
        
        

            
  

Ly = Player(100,"Sword","Lie Lee",50,100)
NPC = Player(50,"Claw","Monster",25,50)

Ly.parry()
print(Ly.remaining_HP)



    


