import pygame
from classes import Snake, Apple

# set window values
WIDTH = 800
HEIGHT = 600


def draw(win, snake, apple):
    win.fill((0, 0, 0))
    snake.draw(win)
    apple.draw(win)
    pygame.display.update()


# the game loop
def main():
    # default "settings"
    score = 0
    fps = pygame.time.Clock()
    run = True

    snake = Snake()
    apple = Apple()

    # draws the window
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    # do this while the game = "run"
    while run:
        # game speed
        fps.tick(15)
        # if X = pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            # snake movement on key_press
            if event.type == pygame.KEYDOWN and event.key:
                snake.directions(event)

        # collision with the apple
        if snake.segments[0][0] == apple.x and snake.segments[0][1] == apple.y:
            score += 1
            snake.grow()
            apple.relocate()

        # collision with outer line of window
        if snake.segments[0][0] >= WIDTH \
                or snake.segments[0][0] < 0 \
                or snake.segments[0][1] >= HEIGHT \
                or snake.segments[0][1] < 0:
            print(score)
            print("Game Over!")
            run = False

        # updates position
        snake.update()
        draw(win, snake, apple)


# calls main loop
main()
