import pygame
import random

from game.components.power_up.shield import *
from game.utils.constants import *

class PowerUpManager:
    def __init__(self):
        shield = Shield()
        burst = Burst()
        freezer = Freezer()
        self.appear_power_up = [shield, burst, freezer]
        self.power_ups = []
        self.when_appears = random.randint(5000, 15000)
        self.duration = random.randint(3,5)

    def generate_power_up(self):
        power_up = Burst()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def update(self,game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.appear_power_up:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up  = True
                game.player.power_up_type = SHIELD_TYPE
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((65,75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)


    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)

