import time
import random
import arcade
from spaceship import Spaceship
from enemy import Enemy
from earth import Earth

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=400, title='Rick and Morty game')
        # arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture('pictures/rick-and-morty-outer-space.jpg')
        self.start_picture = arcade.load_texture('pictures/rick_and_morty.jpg')
        self.me = Spaceship(self.width, 'mamad')
        self.enemy = Enemy(random.randint(100,self.width-100),self.height - 120)
        self.earth = Earth(self.width - 80, 80, 'earth c137')
        self.initial = True

    def on_draw(self):
        arcade.start_render()
        if self.initial:
            arcade.draw_lrwh_rectangle_textured(0, 0, 600, 400, self.start_picture) 
            arcade.draw_text('Rick and Morty', 165, 130, arcade.color.DARK_BLUE, 40, 1, 'left', 'Brush Script MT', True)
            arcade.draw_text('Welcome to MoSa game', 140, 90, arcade.color.DARK_BLUE, 30, 1, 'left', 'Brush Script MT', True)
            arcade.draw_text('press any key to play', 170, 40, arcade.color.BLACK, 20, 1, 'left')
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, 600, 400, self.background)            
            self.me.draw()
            self.enemy.draw()
            self.earth.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # print('symbol key: ',symbol)
        if self.initial:
            self.initial = False
        elif symbol == 97: # left 
            self.me.center_x -= self.me.speed
        elif symbol == 100: # right
            self.me.center_x += self.me.speed
        elif symbol == 119: # up
            self.me.center_y += self.me.speed
        elif symbol == 115: # down
            self.me.center_y -= self.me.speed

    def on_update(self, delta_time):
        self.enemy.move()   

window = Game()
arcade.run()