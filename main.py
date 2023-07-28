import pygame,sys
from settings import Settings
from board import Board
class tic_tac_toe:
    def __init__(self) -> None:
        pygame.init()
        self.player_X=False
        self.setting = Settings()
        self.color = self.setting.color
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.screen.fill(self.setting.bgcolor)
        self.board = Board(self.screen)
    
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
                    print(event.pos)
                    print(position)
                    if self.player_X:
                        ...
                    else:
                        pos = [position[0]+100,position[1]+100]
                        self.board.draw_ring(pos,self.setting.color)
    
    def _update_screen(self):
        self.board.draw_board(self.setting.color)
        self.board.draw_text("Player X chance",self.setting.color)
        pygame.display.flip()

if __name__=="__main__":
    game = tic_tac_toe()
    game.run()