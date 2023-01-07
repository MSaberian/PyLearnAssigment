import random
import arcade
from spaceship import Spaceship

class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(':resources:images/space_shooter/playerShip1_orange.png')
        self.center_x = random.randint(0, w)
        self.center_y = h + 24
        self.width = 48
        self.height = 48
        self.angle = 160
        self.speed = 4

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
                self.me.center_y += self.me.speed
                print('right')

        def on_update(self, delta_time):
            self.enemy.center_y -= self.enemy.speed

window = Game()
arcade.run()