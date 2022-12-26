import pygame

class Ship:
    """
    player model
    """
    def __init__(self, game):
        """sprite and starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # load player
        self.image = pygame.image.load("images/void_ship.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blit(self):
        """
        project player
        """
        self.screen.blit(self.image, self.rect)