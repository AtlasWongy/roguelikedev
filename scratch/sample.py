import numpy as np

# tile_dt = np.dtype(
#     [
#         ("walkable", np.bool)
#     ]
# )
#
#
# def new_tile(
#         *,
#         walkable: int
# ) -> np.ndarray:
#     return np.array(walkable, dtype=tile_dt)
#
#
# def is_walkable(x, y, area):
#     return area["walkable"][x, y]
#
#
# game_map = np.zeros((4, 4), dtype=tile_dt)
#
# game_map[1, 1] = new_tile(walkable=True)
#
# print(game_map["walkable"])


def generate_new_dog(*, breed: str):
    return np.array(breed, dtype=dog_type)


dog_type = np.dtype(
    [
        ("breed", "U20")
    ]
)

cookie = generate_new_dog(breed="Pug")
bobo = generate_new_dog(breed="Maltese")
Keke = generate_new_dog(breed="Doge")

arr = np.array([cookie, bobo, Keke])

print(arr["breed"])







