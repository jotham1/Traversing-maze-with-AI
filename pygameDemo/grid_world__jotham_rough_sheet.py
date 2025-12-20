import pygame
import numpy as np
from typing import Any, List, Tuple


def initialisseGrid(render_mode:str = "human" ):
    pygame.display.set_caption("Simple Gridworld")

    window = None
    clock = None
    window_size = 512
    size = 20
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    RED = (200,0,0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    agent_location = np.array([0, 0])            
    target_location =np.array([size - 1, size - 1])


    if window is None and render_mode == "human":
        pygame.init()
        pygame.display.init()
        window = pygame.display.set_mode((window_size, window_size))
    if clock is None and render_mode == "human":
        clock = pygame.time.Clock()

    canvas = pygame.Surface((window_size, window_size))
    canvas.fill(WHITE)
    pix_square_size = (
        window_size / size
    )  # The size of a single grid square in pixels
            # First we draw the target (green)
    pygame.draw.rect(
        canvas,
        GREEN,
        pygame.Rect(
            pix_square_size * target_location,
            (pix_square_size, pix_square_size),
        ),
    )
    # Now we draw the agent (blue)
    pygame.draw.circle(
        canvas,
        BLUE,
        (agent_location + 0.5) * pix_square_size,
        pix_square_size / 3,
    )



if __name__ == "__main__":
    initialisseGrid()