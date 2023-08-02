player = 'x'
opponent = 'o'
bestmove = (-1,-1)
def evaluate(board_representation):
    #horizontal check
    for i in board_representation:
        if i[0]==i[1] and i[1]==i[2] and i[0]!='_':
            if i[0]==player:
                return 10
            elif i[0]==opponent:
                return -10
    #vertical check
    for i in range(3):
        if board_representation[0][i]==board_representation[1][i] and board_representation[1][i]==board_representation[2][i] and board_representation[0][i]!='_':                
            if board_representation[0][i]==player:
                return 10
            elif board_representation[0][i]==opponent:
                return -10
    #diagonals check
    if board_representation[0][0]==board_representation[1][1] and board_representation[1][1]==board_representation[2][2] and board_representation[0][0]!='_':
        if board_representation[0][0]==player:
            return 10
        elif board_representation[0][0]==opponent:
            return -10
        
    if board_representation[0][2]==board_representation[1][1] and board_representation[1][1]==board_representation[2][0] and board_representation[0][2]!='_':
        if board_representation[0][2]==player:
            return 10
        elif board_representation[0][2]==opponent:
            return -10
    return 0

def isMoveLeft(board_representation):
    for i in board_representation:
        for j in i:
            if j=='_':
                return True
    return False
 
def findBestMove(board_representation):
    best = -1000
    bestmove = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board_representation[i][j]=='_':
                board_representation[i][j]=player
                moveval=minmax(board_representation,True)
                board_representation[i][j]='_'
                if moveval>best:
                    best = moveval
                    bestmove = (i,j)
    return bestmove
def minmax(board_representation,isMax):
    # global bestmove
    score = evaluate(board_representation)
    if score == 10 or score == -10:
        return score
    if isMoveLeft(board_representation) == False:
        return 0
    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board_representation[i][j]=='_':
                    board_representation[i][j] = player
                    best = max(best,minmax(board_representation,not isMax))
                    # moveval = minmax(board_representation,not isMax)
                    # if moveval>best:
                    #     best = moveval
                    #     bestmove = (i,j)
                    board_representation[i][j]='_'
        return best
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board_representation[i][j]=='_':
                    board_representation[i][j] = opponent
                    best = min(best,minmax(board_representation,not isMax))
                    board_representation[i][j]='_'
        return best
    

board_representation = [['x','o','x'],
                      ['_','o','_'],
                      ['_','_','_']]
# a=minmax(board_representation,True)
# print(a)
# print(bestmove)
print(findBestMove(board_representation))