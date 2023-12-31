import pygame,sys
from settings import Settings
from board import Board
from bot import Bot
import minmax

class tic_tac_toe:
    def __init__(self) -> None:
        pygame.init()
        self.player_X=False
        self.is_X_bot = True
        self.playing = True
        self.both_bot = False
        self.bot = Bot()
        self.setting = Settings()
        self.color = self.setting.color
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.screen.fill(self.setting.bgcolor)
        self.board = Board(self.screen)
        self.board.draw_board(self.setting.color)
        if self.player_X:
            self.board.draw_text("Player X chance",self.setting.color)
        else:
            self.board.draw_text("Player O chance",self.setting.color)

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.playing:
                if event.button == 1:
                    position = self.board.which_cell(event.pos[0],event.pos[1])
                    if position==None:
                        break
                    is_empty = self.board.is_empty(position)
                    if self.is_X_bot:
                        if self.player_X:
                            # position = self.bot.bot_choice(self.board.board_representation)
                            position = minmax.findBestMove(self.board.board_representation)
                            if position == (-1,-1):
                                break
                            position=self.board.cords1[position[0]][position[1]]
                            self.player_X_chance(position)
                            self.checkWin("X")
                            self.player_X = False
                        elif (not self.player_X) and is_empty:
                            self.player_O_chance(position)
                            self.checkWin("O")
                            self.player_X = True
                    else:
                        if self.player_X and is_empty:
                            self.player_X_chance(position)
                            self.checkWin("X")
                            self.player_X = False
                        elif (not self.player_X) and is_empty:
                            self.player_O_chance(position)
                            self.checkWin("O")
                            self.player_X = True

    def _update_screen(self):
        pygame.display.flip()
    
    def player_X_chance(self,position):
        pygame.draw.rect(self.screen,self.setting.bgcolor,(0,0,400,50))
        self.board.draw_text("Player O chance",self.setting.color)
        line1 = [[position[0]+40,position[1]+40],[position[0]+160,position[1]+160]]
        line2 = [[position[0]+160,position[1]+40],[position[0]+40,position[1]+160]]   
        self.board.draw_cross(line1,line2,self.setting.color)
        self.board.edit_representation(position,'x')

    def player_O_chance(self,position):
        pygame.draw.rect(self.screen,self.setting.bgcolor,(0,0,400,50))
        self.board.draw_text("Player X chance",self.setting.color)
        pos = [position[0]+100,position[1]+100]
        self.board.draw_ring(pos,self.setting.color)
        self.board.edit_representation(position,'o')

    def checkWin(self,player):
        if self.board.check_win():
            pygame.draw.rect(self.screen,self.setting.bgcolor,(0,0,400,50))
            self.board.draw_text(f"PLAYER {player} WON",self.setting.color)
            self.playing = False

if __name__=="__main__":
    game = tic_tac_toe()
    game.run()