from timeit import repeat
from random import randint
from platform import python_version
from os.path import exists
from os import mkdir

import json

import pygame

def get_random_color() -> tuple[int, int, int]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    
    return (r, g, b)

def fill_surf_with_random_pixels(surf: pygame.Surface) -> None:
    cols, rows = surf.get_size()
    
    for col in range(cols):
        for row in range(rows):
            surf.set_at((col, row), get_random_color())
    
pygame.init()

screen = pygame.display.set_mode((1, 1))

SMALL_SIZE = 10
MEDIUM_SIZE = 100
LARGE_SIZE = 1000

XSMALL_MULTIPLIER = 1.5
SMALL_MULTIPLIER = 2
SUBMEDIUM_MULTIPLIER = 5
MEDIUM_MULTIPLIER = 10
SUPERMEDIUM_MULTIPLIER = 25
LARGE_MULTIPLIER = 50

small_surf = pygame.Surface((SMALL_SIZE, SMALL_SIZE))
fill_surf_with_random_pixels(small_surf)

medium_surf = pygame.Surface((MEDIUM_SIZE, MEDIUM_SIZE))
fill_surf_with_random_pixels(medium_surf)

large_surf = pygame.Surface((LARGE_SIZE, LARGE_SIZE))
fill_surf_with_random_pixels(large_surf)

iterations = 10_000

def time_scale_with_multiplier(surf: pygame.Surface, multiplier: float) -> list[float]:
    print(f"Scaling a surface of size {surf.get_size()} by {multiplier}")
    new_width = surf.get_width() * multiplier
    new_height = surf.get_height() * multiplier
    
    return repeat(lambda : pygame.transform.scale(surf, (new_width, new_height)), repeat=iterations, number=1)

times = {
    "Small Surface": {
        "XSmall Multiplier": time_scale_with_multiplier(small_surf, XSMALL_MULTIPLIER),
        "Small Multiplier": time_scale_with_multiplier(small_surf, SMALL_MULTIPLIER),
        "SubMedium Multiplier": time_scale_with_multiplier(small_surf, SUBMEDIUM_MULTIPLIER),
        "Medium Multiplier": time_scale_with_multiplier(small_surf, MEDIUM_MULTIPLIER),
        "SuperMedium Multiplier": time_scale_with_multiplier(small_surf, SUPERMEDIUM_MULTIPLIER),
        "Large Multiplier": time_scale_with_multiplier(small_surf, LARGE_MULTIPLIER)
    },
    "Medium Surface": {
        "XSmall Multiplier": time_scale_with_multiplier(medium_surf, XSMALL_MULTIPLIER),
        "Small Multiplier": time_scale_with_multiplier(medium_surf, SMALL_MULTIPLIER),
        "SubMedium Multiplier": time_scale_with_multiplier(medium_surf, SUBMEDIUM_MULTIPLIER),
        "Medium Multiplier": time_scale_with_multiplier(medium_surf, MEDIUM_MULTIPLIER),
        "SuperMedium Multiplier": time_scale_with_multiplier(medium_surf, SUPERMEDIUM_MULTIPLIER),
        "Large Multiplier": time_scale_with_multiplier(medium_surf, LARGE_MULTIPLIER)
    },
    "Large Surface": {
        "XSmall Multiplier": time_scale_with_multiplier(large_surf, XSMALL_MULTIPLIER),
        "Small Multiplier": time_scale_with_multiplier(large_surf, SMALL_MULTIPLIER),
        "SubMedium Multiplier": time_scale_with_multiplier(large_surf, SUBMEDIUM_MULTIPLIER),
        "Medium Multiplier": time_scale_with_multiplier(large_surf, MEDIUM_MULTIPLIER),
        "SuperMedium Multiplier": time_scale_with_multiplier(large_surf, SUPERMEDIUM_MULTIPLIER),
        "Large Multiplier": time_scale_with_multiplier(large_surf, LARGE_MULTIPLIER)
    }
}

if not exists("raw_stats"):
    mkdir("raw_stats")

filename = f"raw_stats/({python_version()})"
if not hasattr(pygame, "IS_CE"):
    filename += "pygame-output.json"
else:
    filename += "pygame-ce-output.json"
with open(filename, "w") as dump_file:
    json.dump(times, dump_file, indent=4)