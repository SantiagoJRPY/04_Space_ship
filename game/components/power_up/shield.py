from game.components.power_up.power_up import PowerUp
from game.utils.constants import *

class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD,SHIELD_TYPE)

class Freezer(PowerUp):
    def __init__(self):
        super().__init__(SLOW_IMG,FREZEER)

class Burst(PowerUp):
    def __init__(self):
        super().__init__(BURST_IMG,BURST)


