class PlayerCharacter:
    membership = True  # This is a class attribute

    def __init__(self, name, age=10):

        if (self.membership == True):  # 2 ways to access class attribute - way 1 - "self.membership"
            self.name = name # This is an object attribute, cant access by class name "PlayerCharacter.name"
            self.age = age  # object attribute
       
        elif (PlayerCharacter.membership == False):  # Way 2 - "PlayerCharacter.membership"  (self not required)
            print("Please get a membership")

    def run(self):
        print('word1')
        return self

    def shout(self):
        print(f"your name is {self.name}, You are a member: {PlayerCharacter.membership}")

    @classmethod  # Decorator 1
    def adding_things(cls, num1, num2):
        return cls('jimmy', num1+num2)

    @staticmethod  # Decorator 2
    def adding_things2(num1, num2):
        return num1 + num2


player2 = PlayerCharacter('Jim', 22)
print("Trial 1: ", player2.name, player2.age, player2.run())
print()
print("Trial 2: ", player2.name,  player2.run(),  player2.age)
# Db: Why does this always print 'word1' in the line above and then print other three attributes


player4 = PlayerCharacter('Timmy', 20)

print(player4.run().run().run())
