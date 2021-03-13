class User: # Parent Class
    
    def __init__(self, name, power):
        print('init in User Class')
        self.name = name
        self.power = power
    
    def sign_in(self):
        print('Logged In.')

    def abilities(self):
        print('User has no abilities')

class Wizard (User): # Sub Class / Derived CLass
    def abilities(self): # overriding user's abilities method
        User.abilities(self) # calling parent method inside derived class
        print('Wizard abilities: Ice javelin, Fire bomb')

class Archer (User):
    def __init__ (self, name, power): # method overriding
        print('init in archer class')
        self.name = name
        self.power = power + 1000
    def abilities(self):
        print('Archer abilities: Fire arrow, Earth arrow')


user1 = User('Mini', 100)
print('User: ', user1.name, user1.power)
user1.sign_in()

wizard1 = Wizard('sian',542)
print('Wizard: ', wizard1.name, wizard1.power)
wizard1.sign_in()
wizard1.abilities()

archer1 = Archer('aeon', 777)
print('Archer: ', archer1.name, archer1.power)
archer1.sign_in()
archer1.abilities()



def player_abilities(char):
    char.abilities()

print('player_abilities on wizard object gives abilities of wizard: ')
player_abilities(wizard1)
print('player_abilities on archer object gives abilities of archer: ') 
player_abilities(archer1)
print('We see that the same function gives different results based on the type of object it is passed, this is polymorphism.')
