class Employee:
    
    games = ["Minecraft","Elden Ring","God of War"]
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
class Developer(Employee):
    def __init__(self,first,last,pay,game=[]):
        super().__init__(first,last,pay)
        self.game = []
    def games(self):
        self.game.append(Employee.games)


Ethan = Developer("Ethan", "De Jesus",300000,[])
Ethan.games()
print (Ethan.game)