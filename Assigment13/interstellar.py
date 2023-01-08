import random
import arcade
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=400, title='interstellar game ')
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.me = Spaceship(self.width, 'mamad')
        self.enemy = Enemy(self.width,self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 800, self.background)            
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        print('one key pressed')
        print(symbol)
        if symbol == 97: # left 
            print('left')
            self.me.center_x -= self.me.speed
        elif symbol == 100: # right
            self.me.center_x += self.me.speed
            print('right')

    def on_update(self, delta_time):
        self.enemy.center_y -= self.enemy.speed

window = Game()
arcade.run()