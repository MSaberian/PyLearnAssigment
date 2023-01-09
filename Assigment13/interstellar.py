import random
import arcade
from spaceship import Spaceship
from enemy import Enemy
from earth import Earth

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=400, title='interstellar game ')
        # arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture('pictures/rick-and-morty-outer-space.jpg')
        self.me = Spaceship(self.width, 'mamad')
        self.enemy = Enemy(random.randint(100,self.width-100),self.height - 120)
        self.earth = Earth(self.width - 80, 80, 'earth c137')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 600, 400, self.background)            
        self.me.draw()
        self.enemy.draw()
        self.earth.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        print('symbol key: ',symbol)
        if symbol == 97: # left 
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