from random import choice
class Bot:
    def bot_choice(self,board_cells):
        choices = []
        for i in range(3):
            for j in range(3):
                if board_cells[i][j]=='_':
                    choices.append([(200*j)+50,(200*i)+50])
        return choice(choices)
