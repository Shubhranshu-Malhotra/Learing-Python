class User: # Parent Class
    
    def __init__(self, name, power):
        print('init in User Class')
        self.name = name
        self.power = power
    
    def sign_in(self):
        print('Logged In.')


class Wizard (User): # Sub Class / Derived CLass
    def __init__(self, name, power):
        print('init in Wizard class.')
        self.name = name
        self.power = power
    def abilities(self):
        print('Wizard abilities: Ice javelin, Fire bomb')
    def attack(self):
        print(f'attacking with power of {self.power}')



class Archer (User):
    def __init__ (self, name, arrows):
        print('init in archer class')
        self.name = name
        self.arrows = arrows
    def abilities(self):
        print('Archer abilities: Fire arrow, Earth arrow')
    def check_arrows(self):
        print(f'{self.arrows} remaining')
    def run(self):
        print('runs really fast.')

class HyBorg(Wizard, Archer):
    def __init__ (self, name, power, arrows):
        # Wizard.__init__
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HyBorg('borgie', 100, 20)
hb1.check_arrows()
print(hb1.name)
hb1.attack()
hb1.sign_in()