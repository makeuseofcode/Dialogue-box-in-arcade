import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

blue = arcade.color.BLUE
green = arcade.color.GREEN

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.platform_x = SCREEN_WIDTH // 2
        self.platform_y = SCREEN_HEIGHT // 4

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, self.player_y, 50, 50, blue)
        arcade.draw_rectangle_filled(self.platform_x, self.platform_y, 200, 20, green)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 25
        elif key == arcade.key.RIGHT:
            self.player_x += 25
        elif key == arcade.key.UP:
            self.player_y += 25
        elif key == arcade.key.DOWN:
            self.player_y -= 25

    def on_key_release(self, key, modifiers):
        pass

    def update(self, delta_time):
        pass

def main():
    game = Game()
    arcade.run()

if __name__ == "__main__":
    main()
