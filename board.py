import pygame
class Board:
    def __init__(self,screen) -> None:
        self.screen = screen
        self.board_representation = [['_','_','_',],
                      ['_','_','_',],
                      ['_','_','_',]]
        self.cords = {[50,50]:0,[250,50]:1,[450,50]:2,[50,250]:3,[250,250]:4,[450,250]:5,[50,450]:6,[250,450]:7,[450,450]:8}
        
    def draw_ring(self,position):
        pygame.draw.circle(self.screen,self.color,position,40)
        pygame.draw.circle(self.screen,(0,0,0),position,35)
    
    def draw_cross(self,dig1:list,dig2:list):
        pygame.draw.line(self.screen,self.color,dig1[0],dig1[1],5)
        pygame.draw.line(self.screen,self.color,dig2[0],dig2[1],5)
    
    def draw_text(self,text):
        img = self.font.render(text,True,self.color)
        self.screen.blit(img,(5,5))
    