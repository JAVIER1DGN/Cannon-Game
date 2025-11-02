import arcade
from arcade.physics_engines import PhysicsEngineSimple

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Moving Block Game"

# Constants for block movement
MOVEMENT_SPEED = 5
WALL_THICKNESS = 20

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set up the game background
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Sprite lists
        self.block_list = None
        self.wall_list = None
        
        # Player sprite
        self.block = None
        
        # Physics engine
        self.physics_engine = None

    def setup(self):
        # Create sprite lists
        self.block_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        
        # Create walls
        # Bottom wall
        bottom = arcade.SpriteSolidColor(SCREEN_WIDTH, WALL_THICKNESS, arcade.color.DARK_GREEN)
        bottom.center_x = SCREEN_WIDTH // 2
        bottom.center_y = WALL_THICKNESS // 2
        self.wall_list.append(bottom)
        
        # Top wall
        top = arcade.SpriteSolidColor(SCREEN_WIDTH, WALL_THICKNESS, arcade.color.DARK_GREEN)
        top.center_x = SCREEN_WIDTH // 2
        top.center_y = SCREEN_HEIGHT - WALL_THICKNESS // 2
        self.wall_list.append(top)
        
        # Left wall
        left = arcade.SpriteSolidColor(WALL_THICKNESS, SCREEN_HEIGHT, arcade.color.DARK_GREEN)
        left.center_x = WALL_THICKNESS // 2
        left.center_y = SCREEN_HEIGHT // 2
        self.wall_list.append(left)
        
        # Right wall
        right = arcade.SpriteSolidColor(WALL_THICKNESS, SCREEN_HEIGHT, arcade.color.DARK_GREEN)
        right.center_x = SCREEN_WIDTH - WALL_THICKNESS // 2
        right.center_y = SCREEN_HEIGHT // 2
        self.wall_list.append(right)
        
        # Create player block
        self.block = arcade.SpriteSolidColor(50, 50, arcade.color.RED)
        self.reset_block_position()
        self.block_list.append(self.block)
        
        # Create physics engine without gravity
        self.physics_engine = PhysicsEngineSimple(
            self.block,
            self.wall_list
        )

    def reset_block_position(self):
        """Reset the block to the center of the screen"""
        self.block.center_x = SCREEN_WIDTH // 2
        self.block.center_y = SCREEN_HEIGHT // 2
        self.block.change_x = 0
        self.block.change_y = 0

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.block_list.draw()
        
        # Draw instructions
        arcade.draw_text("Use Arrow Keys to move \nPress R to reset",
                        SCREEN_WIDTH - 1200, SCREEN_HEIGHT - 60,
                        arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.block.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.block.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.block.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.block.change_x = MOVEMENT_SPEED
        elif key == arcade.key.R:  # Reset game
            self.reset_block_position()

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.block.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.block.change_y = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
