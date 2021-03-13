class User:
    
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def sign_in(self):
        print('Logged In.')

class Wizard (User):
    # def __init__(self, name, power):
    #     self.name = name
    #     self.power = power
    def abilities(self):
        print('Wizard abilities: Ice javelin, Fire bomb')

class Archer (User):
    # def __init__(self, name, num_arrows):
    #     self.name = name
    #     self.power = power
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
