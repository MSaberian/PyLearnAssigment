import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, w, name: str):
        super().__init__('pictures/rick spaceship_low.png')
        self.center_x = w // 2
        self.center_y = 80
        self.width = 100
        self.height = 60
        self.name = name
        self.speed = 8
