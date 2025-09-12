import arcade
from main_project.game.structure import map

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Cannon Game"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("¡Hola Arcade!", 100, 300, arcade.color.WHITE, 24)

if __name__ == "__main__":
    window = MyGame()
    arcade.run()
