import pygame
import random


# snake + behaviour
class Snake:
    def __init__(self):
        self.color = (0, 255, 0)
        self.step_size = 20
        # direction of the snake
        self.direct = [1, 0]
        # starting position + length
        self.segments = [[400, 300], [380, 300]]
        # checks if the apple has been eaten
        self.add_seg = False

    # directions based on key_press
    def directions(self, event):
        if event.key == pygame.K_LEFT:
            if self.direct[0] != 1:
                self.direct[0] = -1
                self.direct[1] = 0

        elif event.key == pygame.K_RIGHT:
            if self.direct[0] != -1:
                self.direct[0] = 1
                self.direct[1] = 0

        elif event.key == pygame.K_UP:
            if self.direct[1] != 1:
                self.direct[1] = -1
                self.direct[0] = 0

        elif event.key == pygame.K_DOWN:
            if self.direct[1] != -1:
                self.direct[1] = 1
                self.direct[0] = 0

    # defines the growth
    def grow(self):
        self.add_seg = True

    # updates location of snake
    def update(self):
        self.segments.reverse()
        # saves position off last segment
        last_seg = self.segments[0].copy()

        for count, seg in enumerate(self.segments):
            if not len(self.segments) == count + 1:
                self.segments[count] = self.segments[count + 1].copy()

            else:
                # normal movement
                self.segments[count][0] += self.step_size * self.direct[0]
                self.segments[count][1] += self.step_size * self.direct[1]

                # checks for self-collision
                for count_dracula, segmund in enumerate(self.segments):
                    if not len(self.segments) == count_dracula + 1:
                        # checks for the self position off segments
                        if segmund[0] == self.segments[count][0] and segmund[1] == self.segments[count][1]:
                            print("Game Over!!!")
                            quit()

        # reverses snake from last segment position
        self.segments.reverse()

        # appends segment to snake :3
        if self.add_seg:
            self.segments.append(last_seg)
            self.add_seg = False

    # draw the snake on the screen
    def draw(self, win):
        # draws snake and extra segments
        for seg in self.segments:
            pygame.draw.rect(win, self.color, [seg[0], seg[1], 20, 20])


class Apple:
    def __init__(self):
        self.color = (255, 0, 0)
        # initial spawn
        self.x = random.randrange(0, 40) * 20
        self.y = random.randrange(0, 30) * 20

    # if apple has been eaten relocate to random place on grid
    def relocate(self):
        self.x = random.randrange(0, 40) * 20
        self.y = random.randrange(0, 30) * 20

    # draws the apple
    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, 20, 20])
