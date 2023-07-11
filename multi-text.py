import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.platform_x = SCREEN_WIDTH // 2
        self.platform_y = SCREEN_HEIGHT // 4
        self.dialogue_active = False
        self.dialogue_messages = [
            "Hello, player! How are you?",
            "Nice weather today, isn't it?",
            "Beware of the enemies lurking ahead!"
        ]
        self.dialogue_index = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.dialogue_active:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.dialogue_index = (self.dialogue_index + 1) % len(self.dialogue_messages)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, self.player_y, 50, 50, arcade.color.BLUE)
        arcade.draw_rectangle_filled(self.platform_x, self.platform_y, 200, 20, arcade.color.GREEN)
        if self.dialogue_active:
            self.draw_dialogue_box()
    
    def draw_dialogue_box(self):
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 500, 200, arcade.color.WHITE)
        arcade.draw_text(self.dialogue_messages[self.dialogue_index], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20,
                         arcade.color.BLACK, font_size=16, anchor_x="center", anchor_y="center")
        arcade.draw_text("Next", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, arcade.color.BLACK, font_size=16,
                         anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 25
        elif key == arcade.key.RIGHT:
            self.player_x += 25
        elif key == arcade.key.UP:
            self.player_y += 25
        elif key == arcade.key.DOWN:
            self.player_y -= 25
        elif key == arcade.key.SPACE:
            self.dialogue_index +=1
            if self.dialogue_index >= len(self.dialogue_messages):
                self.dialogue_index = 0

    def on_key_release(self, key, modifiers):
        pass

    def update(self, delta_time):
        if self.check_enemy_collision():
            self.dialogue_active = True
    def check_enemy_collision(self):
        player_radius = 25
        distance_x = abs(self.player_x - self.platform_x)
        distance_y = abs(self.player_y - self.platform_y)
        combined_radius = player_radius + 25

        if distance_x < combined_radius and distance_y < combined_radius:
            return True
        else:
            return False

def main():
    game = Game()
    arcade.run()

if __name__ == "__main__":
    main()
