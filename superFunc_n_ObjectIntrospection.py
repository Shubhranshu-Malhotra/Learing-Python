class User ():
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('Loggen in!')

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmailc.com')
wizard1.sign_in()
print(wizard1.email) # throws error if `User.__init__()` or super not called in wizard class

# introspection
print(dir(wizard1)) # to get list of methods, func, attr. the instance has access to