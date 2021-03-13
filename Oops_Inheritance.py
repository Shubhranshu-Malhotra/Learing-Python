class User: # Parent Class
    
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def sign_in(self):
        print('Logged In.')

class Wizard (User): # Sub Class / Derived CLass
    def abilities(self):
        print('Wizard abilities: Ice javelin, Fire bomb')

class Archer (User):
    def abilities(self):
        print('Archer abilities: Fire arrow, Earth arrow')

user1 = User('Mini', 100)
# user1 = User()
print('User: ', user1.name, user1.power)
user1.sign_in()

wizard1 = Wizard('sian',542)
archer1 = Archer('aeon', 777)
print('Wizard: ', wizard1.name, wizard1.power)
wizard1.sign_in()
wizard1.abilities()
print('Archer: ', archer1.name, archer1.power)
archer1.sign_in()
archer1.abilities()


print('Checking instace of which classes')
print('Check if wizard1 is instance of Wizard Class: ', isinstance(wizard1, Wizard))
print('Check if wizard1 is instance of User Class: ', isinstance(wizard1, User))
print('Check if wizard1 is instance of object Class: ', isinstance(wizard1, object))
print('Check if wizard1 is instance of Archer Class: ', isinstance(wizard1, Archer))
print('Check if Archer is instance of object Class: ', isinstance(Archer, object))


