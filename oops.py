class PlayerCharacter:
    def __init__(self, name):
        self.name = name
    def run(self):
        print('run')

player1 = PlayerCharacter('Anna')
print(player1.name)