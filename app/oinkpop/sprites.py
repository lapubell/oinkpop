import arcade

class Oink(arcade.Sprite):
    """
    Player Class
    """

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
