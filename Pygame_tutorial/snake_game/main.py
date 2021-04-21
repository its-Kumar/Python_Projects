### Libraries ###
import random
import time

import pygame
from pygame.locals import *

### Globals ###
SIZE = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

### Apple class ###


class Apple:

    # initialize apple object
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, (SCREEN_WIDTH // 40) - 1) * SIZE
        self.y = random.randint(0, (SCREEN_HEIGHT // 40) - 1) * SIZE


### End of Apple ###


### Snake class ###
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "down"
        self.length = length

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE
        self.draw()


### End of Snake ###


### Game class ###
class Game:

    # initalize the game
    def __init__(self, x, y):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Snake Game by Kumar Shanu")
        self.play_bakground_music()
        self.score = 0
        self.surface = pygame.display.set_mode((x, y))
        self.render_background()
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    # reset the game
    def reset(self):
        self.score = 0
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)

    # detect collision
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    # play the sounds
    def play_sound(self, sound_name):
        pygame.mixer.music.pause()
        if sound_name == "die":
            sound = pygame.mixer.Sound("resources/die_sound.ogg")
        elif sound_name == "eat":
            sound = pygame.mixer.Sound("resources/eat.ogg")
        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.unpause()

    # play the background music
    def play_bakground_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play(100)

    def increase_speed(self):
        if self.score < 5:
            s = 0.4
        elif self.score < 10:
            s = 0.3
        elif self.score < 20:
            s = 0.25
        elif self.score < 25:
            s = 0.2
        elif self.score < 30:
            s = 0.15
        else:
            s = 0.1
        time.sleep(s)

    # play the game
    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating the apple
        # snake colliding with apple
        if self.is_collision(
            self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y
        ):
            self.play_sound("eat")
            self.score += 1
            self.snake.increase_length()
            self.apple.move()
            print(f"Score : {self.score}")

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(
                self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]
            ):
                raise Exception("Game Over")

        # snake colliding with the walls
        if self.snake.x[0] <= 0 - SIZE:
            self.snake.x[0] = 0
            raise Exception("Game Over")
        elif self.snake.x[0] >= SCREEN_WIDTH:
            self.snake.x[0] = SCREEN_WIDTH - SIZE
            raise Exception("Game Over")
        if self.snake.y[0] <= 0 - SIZE:
            self.snake.y[0] = 0
            raise Exception("Game Over")
        elif self.snake.y[0] >= SCREEN_HEIGHT:
            self.snake.y[0] = SCREEN_HEIGHT - SIZE
            raise Exception("Game Over")

    # display score on the screen
    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score : {self.score}", True, (200, 200, 200))
        self.surface.blit(score, (650, 10))

    # start the game
    def run(self):
        running = True
        pause = False
        while running:
            # check for the events
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                # detect key press event
                if event.type == KEYDOWN:
                    # restart the game
                    if event.key == K_RETURN and pause:
                        pause = False
                        pygame.mixer.music.unpause()
                        self.reset()
                    # exit the game
                    if event.key == K_ESCAPE:
                        running = False

                    if not pause:
                        # move the snake with keys
                        if event.key == K_UP:
                            if not self.snake.direction == "down":
                                self.snake.move_up()
                        if event.key == K_DOWN:
                            if not self.snake.direction == "up":
                                self.snake.move_down()
                        if event.key == K_LEFT:
                            if not self.snake.direction == "right":
                                self.snake.move_left()
                        if event.key == K_RIGHT:
                            if not self.snake.direction == "left":
                                self.snake.move_right()
            try:
                if not pause:
                    self.play()

            # Game Over
            except Exception as e:
                if e.args[0] == "Game Over":
                    self.play_sound("die")
                    self.show_game_over()
                    pause = True
                print(e)
            self.increase_speed()

    # show game over on screen
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render(
            f"Game is over! Your score is {self.score}", True, (255, 255, 255)
        )
        self.surface.blit(line1, (150, 300))
        line2 = font.render(
            "To play again press Enter, To exit press Escape!", True, (255, 255, 255)
        )
        self.surface.blit(line2, (150, 360))
        pygame.display.flip()
        pygame.mixer.music.pause()


### End of Game ###

### main function ###
if __name__ == "__main__":
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()

### End of main function ###
