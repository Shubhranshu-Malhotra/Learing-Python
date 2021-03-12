class PlayerCharacter:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Anna')
print("Player 1 Details: ",player1.name, player1.age)
player2 = PlayerCharacter('Rohan', 22)
# print("Player 2 Details: ", player2.name, player2.age, player2.run())
print(player2.name,  player2.run(),  player2.age)
player2.attack = 150
print(player2.attack)
print(player1.attack) # throws error since attack attribute defined only for player 2