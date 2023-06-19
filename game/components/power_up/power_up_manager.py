import pygame
import random

from game.components.power_up.shield import *
from game.utils.constants import *
from game.components.bullets.bullet_manager import BulletManager

class PowerUpManager:
    def __init__(self):
        self.bullet_manager = BulletManager()
        self.shield = Shield()
        self.burst = Burst()
        self.appear_power_up = [self.shield, self.burst]
        self.power_ups = []
        self.when_appears = random.randint(5000, 15000)
        self.duration = random.randint(5,10)

    def generate_power_up(self):
        power_up = random.choice(self.appear_power_up)
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def update(self,game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up) and power_up == self.shield:
                print("Colisiono con Shield")
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up  = True
                game.player.power_up_type = SHIELD_TYPE
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((65,75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
            
            elif game.player.rect.colliderect(power_up) and power_up == self.burst:
                print("Colisiono con Burst")
                game.player.total_bullet = 4
                print(game.player.total_bullet)
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up  = True
                game.player.power_up_type = BURST
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((65,75), SPACESHIP_BURST)
                self.power_ups.remove(power_up)
                
            
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)

