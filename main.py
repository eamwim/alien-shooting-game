import pygame
import sys
from settings import Settings
from ship import Ship

class Alien_Game:
    """
    manage game behavior
    """
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        self.ship = Ship(self)
        pygame.display.set_caption("alien game")

    def run_game(self):
        """
        main loop
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # make the most recently drawn screen visible.
            self.screen.fill(self.settings.bgc)
            self.ship.blit()
            pygame.display.flip()

if __name__ == "__main__":
    ag = Alien_Game()
    ag.run_game()
