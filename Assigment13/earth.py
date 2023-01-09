import arcade

class Earth(arcade.Sprite):
    def __init__(self, x, y, name: str):
        super().__init__('pictures/earth_low.png')
        self.center_x = x
        self.center_y = y
        self.width = 80
        self.height = 80
        self.name = name
        self.speed = 8
