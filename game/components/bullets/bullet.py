import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    X_POS = 80
    Y_POS = 310
    SPEED = 20
    BULLET_SYZE = pygame.transform.scale(BULLET, (10,20))
    BULLET_SYZE_ENEMY = pygame.transform.scale(BULLET_ENEMY, (9,32))
    BULLETS = {'player':BULLET_SYZE, 'enemy':BULLET_SYZE_ENEMY}


    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type


    def events(self):
        pass
    def update(self, bullets):
        for bullet in bullets:
            if bullet.owner == 'enemy':
                self.rect.y += self.SPEED
                if self.rect.y >= SCREEN_HEIGHT:
                    bullets.remove(self)
            if bullet.owner == 'player':
                self.rect.y -= self.SPEED
                if self.rect.y < 0:
                    bullets.remove(self)
    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))