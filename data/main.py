from material.game.structure.map import MyGame
import arcade

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
