import numpy as np
from tcod.console import Console

import tiles_type


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tiles_type.floor, order="F")

        self.tiles[30:33, 22] = tiles_type.wall

        # Continue tmr