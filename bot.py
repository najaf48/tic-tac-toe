from random import choice
class Bot:
    def __init__(self):
        self.cords = [[50,50],[250,50],[450,50],[50,250],[250,250],[450,250],[50,450],[250,450],[450,450]]
    
    def bot_choice(self,board_cells):
        choices = []
        print(board_cells)
        for i in range(3):
            for j in range(3):
                if board_cells[i][j]=='_':
                    choices.append([(200*j)+50,(200*i)+50])
        return choice(choices)
