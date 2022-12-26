import pygame
import sys

class alien_game:
    """
    manage game behavior
    """
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
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
            pygame.display.flip()

if __name__ == "__main__":
    ag = alien_game()
    ag.run_game()
