# Udemy: Python Developer in 2021: Zero to Mastery

# Lecture 116, 117


class PlayerCharacter:
    membership = True # This is a class attribute
    def __init__(self, name, age=10):
        if (self.membership == True): # 2 ways to access class attribute - way 1 - "self.membership" 
            self.name = name # This is an object attribute, cant access by class name "PlayerCharacter.name"
            self.age = age # object attribute
        elif (PlayerCharacter.membership == False): # Way 2 - "PlayerCharacter.membership"  (self not required)
            print("Please get a membership")
    def run(self):
        print('run')
        return 'done'
    def shout(self):
        print(f"your name is {self.name}, You are a member: {PlayerCharacter.membership}")
player1 = PlayerCharacter('Anna')
print("Player 1 Details: ",player1.name, player1.age)
player2 = PlayerCharacter('Rohan', 22)
# print("Player 2 Details: ", player2.name, player2.age, player2.run())
print(player2.name,  player2.run(),  player2.age)
player2.attack = 150
print(player2.attack)
player1.shout()
# print(player1.attack) # throws error since attack attribute defined only for player 2


# Lecture 117




