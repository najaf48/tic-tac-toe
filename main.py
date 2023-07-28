import pygame,sys
from settings import Settings
from board import Board
class tic_tac_toe:
    def __init__(self) -> None:
        pygame.init()
        self.player_X=True
        self.setting = Settings()
        self.color = self.setting.color
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.screen.fill(self.setting.bgcolor)
        self.board = Board(self.screen)
        self.board.draw_board(self.setting.color)
        self.board.draw_text("Player X chance",self.setting.color)
    
    def run(self):
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position=self.board.which_cell(event.pos[0],event.pos[1])
                    is_occupied = self.board.is_occupied(position)
                    if self.player_X and self.board.is_occupied(position):
                        
                        pygame.draw.rect(self.screen,self.setting.bgcolor,(0,0,400,50))
                        self.board.draw_text("Player O chance",self.setting.color)
                        
                        line1 = [[position[0]+40,position[1]+40],[position[0]+160,position[1]+160]]
                        line2 = [[position[0]+160,position[1]+40],[position[0]+40,position[1]+160]]
                        
                        self.board.draw_cross(line1,line2,self.setting.color)
                        
                        self.board.edit_representation(position,'x')
                        self.player_X = False

                    elif (not self.player_X) and self.board.is_occupied(position):
                        
                        pygame.draw.rect(self.screen,self.setting.bgcolor,(0,0,400,50))
                        self.board.draw_text("Player X chance",self.setting.color)
                        
                        pos = [position[0]+100,position[1]+100]
                        self.board.draw_ring(pos,self.setting.color)
                        
                        self.board.edit_representation(position,'o')
                        self.player_X = True

    def _update_screen(self):
        pygame.display.flip()

if __name__=="__main__":
    game = tic_tac_toe()
    game.run()