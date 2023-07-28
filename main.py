import pygame,sys
from settings import Settings

class tic_tac_toe:
    def __init__(self) -> None:
        pygame.init()
        self.font = pygame.font.SysFont(None, 50,bold=False)
        self.setting = Settings()
        self.color = self.setting.color
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.screen.fill(self.setting.bgcolor)
    
    def run(self):
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ...
    
    def _update_screen(self):
        self.draw_text("hello")
        pygame.display.flip()
    
    def draw_ring(self,position):
        pygame.draw.circle(self.screen,self.color,position,40)
        pygame.draw.circle(self.screen,(0,0,0),position,35)
    
    def draw_cross(self,dig1:list,dig2:list):
        pygame.draw.line(self.screen,self.color,dig1[0],dig1[1],5)
        pygame.draw.line(self.screen,self.color,dig2[0],dig2[1],5)
    def draw_text(self,text):
        img = self.font.render(text,True,self.color)
        self.screen.blit(img,(5,5))
        pygame.draw.rect(self.screen,self.color,(50,50,600,600))

if __name__=="__main__":
    game = tic_tac_toe()
    game.run()