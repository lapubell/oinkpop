import arcade
from oinkpop.sprites import Oink

class MyGame(arcade.Window):
    """
    Main application class
    """

    def __init__(self, width, height, title, speed):
        super().__init__(width, height, title)
        self.movement_speed = speed

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = Oink("images/oink-frame-1.png", 0.5)
        self.player_sprite.center_x = self.width/2
        self.player_sprite.center_y = self.height/2
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = self.movement_speed
        if key == arcade.key.DOWN:
            self.player_sprite.change_y = self.movement_speed * -1
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = self.movement_speed * -1
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = self.movement_speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        if key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
