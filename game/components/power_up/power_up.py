import random, pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.image = pygame.transform.scale(self.image, (30,30))
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH -120)
        self.rect.y = 0
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y < 0  or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)
            print("Desaparecio")
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)

