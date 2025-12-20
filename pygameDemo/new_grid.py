import numpy as np  
import pygame
import time
import matplotlib.pyplot as plt

class Grid:
    def __init__(self, height, width, start=(0, 0), goal=None, obstacles=None):
        self.h = height
        self.w = width
        self.start = start
        self.goal = goal if goal is not None else (height - 1, width - 1)
        self.obstacles = set(obstacles) if obstacles else set()
        self.agent_pos = None
        
        # Pygame variables (initialized lazily)
        self._screen = None
        self._cell_size = 40
        self._margin = 2

    def state_index(self, pos):
        r, c = pos
        return r * self.w + c

    def is_valid(self, pos):
        r, c = pos
        if r < 0 or r >= self.h or c < 0 or c >= self.w:
            return False
        return pos not in self.obstacles

    def reset(self, random_start=False):
        if random_start:
            free = [(r, c) for r in range(self.h) for c in range(self.w)
                    if (r, c) not in self.obstacles and (r, c) != self.goal]
            self.agent_pos = tuple(free[np.random.randint(len(free))])
        else:
            self.agent_pos = self.start if self.is_valid(self.start) else self.goal
        return self.state_index(self.agent_pos)

    def step(self, action):
        """SUBROUTINE INTEGRITY: Logic for move/reward exactly as provided."""
        r, c = self.agent_pos
        if action == 0:   new = (r - 1, c) # up
        elif action == 1: new = (r, c + 1) # right
        elif action == 2: new = (r + 1, c) # down
        elif action == 3: new = (r, c - 1) # left
        else:             new = (r, c)

        if not self.is_valid(new):
            return self.state_index(self.agent_pos), -5.0, False

        self.agent_pos = new
        next_s = self.state_index(new)

        if new == self.goal:
            return next_s, 100.0, True
        return next_s, -1.0, False

    def render(self, q_table=None, delay=0.05):
        if self._screen is None:
            pygame.init()
            tw = self.w * (self._cell_size + self._margin) + self._margin
            th = self.h * (self._cell_size + self._margin) + self._margin
            self._screen = pygame.display.set_mode((tw, th))
            pygame.display.set_caption("Gridworld")

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return

        self._screen.fill((50, 50, 50))
        for r in range(self.h):
            for c in range(self.w):
                rect = pygame.Rect(self._margin + c*(self._cell_size+self._margin), 
                                   self._margin + r*(self._cell_size+self._margin), 
                                   self._cell_size, self._cell_size)
                color = (200, 200, 200)
                if (r, c) in self.obstacles: color = (40, 40, 40)
                elif (r, c) == self.goal: color = (50, 200, 50)
                elif (r, c) == self.start: color = (50, 50, 200)
                pygame.draw.rect(self._screen, color, rect)

                if q_table is not None and (r, c) not in self.obstacles:
                    s = self.state_index((r, c))
                    best_a = int(np.argmax(q_table[s]))
                    # Arrow drawing logic... (omitted for brevity, same as original)

        if self.agent_pos:
            r, c = self.agent_pos
            rect = pygame.Rect(self._margin + c*(self._cell_size+self._margin), 
                               self._margin + r*(self._cell_size+self._margin), 
                               self._cell_size, self._cell_size)
            pygame.draw.circle(self._screen, (255, 0, 0), rect.center, 15)
        pygame.display.flip()
        time.sleep(delay)
