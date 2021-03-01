import arcade
from oinkpop.app import MyGame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "OinkPOP"
MOVEMENT_SPEED = 5

game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, MOVEMENT_SPEED)
game.setup()

arcade.run()
