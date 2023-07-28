import pygame
class Board:
    def __init__(self,screen) -> None:
        self.screen = screen
        self.board_representation = [['_','_','_',],
                      ['_','_','_',],
                      ['_','_','_',]]
        self.font = pygame.font.SysFont(None, 50,bold=False)
        self.cords = [[50,50],[250,50],[450,50],[50,250],[250,250],[450,250],[50,450],[250,450],[450,450]]
        self.cords1 = [[[50,50],[250,50],[450,50]],
                       [[50,250],[250,250],[450,250]],
                       [[50,450],[250,450],[450,450]]]

    
    def draw_board(self,color:tuple):
        # self.screen.fill((0,0,0))
        pygame.draw.line(self.screen,color,[250,50],[250,650],3)
        pygame.draw.line(self.screen,color,[450,50],[450,650],3)
        pygame.draw.line(self.screen,color,[50,250],[650,250],3)
        pygame.draw.line(self.screen,color,[50,450],[650,450],3)
    
    def draw_ring(self,position:list,color):
        pygame.draw.circle(self.screen,color,position,60)
        pygame.draw.circle(self.screen,(0,0,0),position,55)
    
    def draw_cross(self,line1:list,line2:list,color:tuple):
        pygame.draw.line(self.screen,color,line1[0],line1[1],5)
        pygame.draw.line(self.screen,color,line2[0],line2[1],5)
    
    def draw_text(self,text:str,color:tuple):
        img = self.font.render(text,True,color)
        self.screen.blit(img,(5,5))
    
    def is_occupied(self,cord):
        i = int((cord[0]-50)/200)
        j = int((cord[1]-50)/200)
        if self.board_representation[j][i]=='_':
            return True
        else:
            return False
    def edit_representation(self,cord,symbol):
        for i in range(3):
            for j in range(3):
                if cord == [(200*i)+50,(200*j)+50]:
                    self.board_representation[j][i]=symbol

    def which_cell(self,x,y):
        for cord in self.cords:
            if (x>cord[0] and x<(cord[0]+200)) and (y>cord[1] and y<(cord[1]+200)):
                return cord
    