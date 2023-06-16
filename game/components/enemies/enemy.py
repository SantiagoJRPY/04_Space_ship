import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_2, ENEMY_3, ENEMY_4
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    Y_POS = 20
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550]
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X = {0:'left', 1:'right'}
    IMAGE = {1:ENEMY_1, 2:ENEMY_2, 3:ENEMY_3, 4:ENEMY_4,}
    MOV_LEFT = 0
    MOV_RIGHT = 0

    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = (30,100)):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0,10)]
        self.rect.y = self.Y_POS
        self.type = 'enemy'

        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.shooting_time = random.randint(30,50)

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH):
            self.movement_x = 'left'
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'

        if self.index >= self.move_x_for:
            self.index = 0


    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
            self.MOV_LEFT += 1
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()
            self.MOV_RIGHT += 1
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(20,50)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

