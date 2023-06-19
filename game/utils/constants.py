import pygame
import os


pygame.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SLOW_IMG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Slow.png'))
BURST_IMG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Burst.jpg'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
FREZEER = 'freezer'
BURST = 'burst'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_BURST = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/Spaceship_Burst.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))

SOUND_SHOTS = pygame.mixer.Sound('game/assets/Sounds/laser2.wav')
BACKGROUND_SOUND_START = pygame.mixer.Sound('game/assets/Sounds/Nebulous.mp3')
BACKGROUND_SOUND_END = pygame.mixer.Sound('game/assets/Sounds/End.ogg')

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
BACKGROUND_START1 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/Background1.png"))




FONT_STYLE = 'freesansbold.ttf'
FONT_VERDANA = pygame.font.SysFont("verdana", 40)
