# Udemy: Python Developer in 2021: Zero to Mastery

# Lecture 116, 117, 120


class PlayerCharacter:
    membership = True  # This is a class attribute

    def __init__(self, name, age=10):
        if (self.membership == True):   # 2 ways to access class attribute - way 1 - "self.membership"
            self.name = name  # This is an object attribute, cant access by class name "PlayerCharacter.name"
            self.age = age  # object attribute
        
        elif (PlayerCharacter.membership == False):   # Way 2 - "PlayerCharacter.membership"  (self not required)
            print("Please get a membership")

    def run(self):
        print('run')
        return self

    def shout(self):
        print(f"your name is {self.name}, You are a member: {PlayerCharacter.membership}")

    @classmethod # Decorator 1
    def adding_things(cls, num1, num2):
        return cls('jimmy', num1+num2)

    @staticmethod # Decorator 2
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Anna')
print("Player 1 Details: ", player1.name, player1.age)
player2 = PlayerCharacter('Rohan', 22)
# print("Player 2 Details: ", player2.name, player2.age, player2.run())
print(player2.name,  player2.run(),  player2.age)
player2.attack = 150
print(player2.attack)
player1.shout()
# print(player1.attack) # throws error since attack attribute defined only for player 2

# using @classmethod
player3 = PlayerCharacter.adding_things(2,3)
print("adding_things is a class method, it instaniates a class object (can do because has class as a parameter) and gives it a name and age")
print("name and age using adding_things: ",player3.name, player3.age)

#using @staticmethod
print("adding_things2 is a static method it cannot instantiate a class object (doesn't have class as parameter)")
print("adding_things2 just performs addition in two numbers: ", PlayerCharacter.adding_things2(4,3))

