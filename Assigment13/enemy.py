import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, x, h):
        super().__init__('pictures/enemy_spaceship_low.png')
        # super().__init__(':resources:images/space_shooter/playerShip1_orange.png')
        self.center_x = x
        self.center_y = h + 24
        self.width = 80
        self.height = 80
        self.angle = 160
        self.speed = 1
        self.orientation = 'left'

    def move(self):
        if self.center_x == 100:
            self.orientation = 'right'
        elif self.center_x == 500:
            self.orientation = 'left'
        if self.orientation == 'left':
            self.center_x -= self.speed
        elif self.orientation == 'right':
            self.center_x += self.speed
