"""
DotDict Borrowed from here:
https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary/28463329

Does not impact code, simply makes it easier to read. Converts Dictionary to class to allow for dot notation
"""

import arcade


class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


# Game Screen
SCREEN = {
    "WIDTH": 800,
    "HEIGHT": 600,
    "COLOR": arcade.color.SMOKY_BLACK
}

# Bullet
BULLET = {
    "RADIUS": 30,
    "WIDTH": 10,
    "HEIGHT": 40,
    "SPEED": 10,
    "LIFE": 60,
    "IMG": "images/missile.png"
}

# Ship
SHIP = {
    "TURN_AMOUNT": 3,
    "THRUST_AMOUNT": 0.25,
    "RADIUS": 30,
    "IMG": "images/playerShip1_orange.png"
}

# Rocks
ROCK = {
    "INITIAL_ROCK_COUNT": 5,
}

LARGE_ROCK = {
    "SPEED": 1.5,
    "SPIN": 1,
    "RADIUS": 45,
    "IMG": "images/meteorGrey_big1.png"
}

MEDIUM_ROCK = {
    "SPIN": -2,
    "RADIUS": 30,
    "IMG": "images/meteorGrey_med1.png"
}

SMALL_ROCK = {
    "SPIN": 5,
    "RADIUS": 15,
    "IMG": "images/meteorGrey_small1.png"
}

EXPLOSION = {
    "FRAMES": 9,
    "DELAY": 5,
    "SIZE": 45,
    "IMG": [
        "images/explosion/001.png",
        "images/explosion/002.png",
        "images/explosion/003.png",
        "images/explosion/004.png",
        "images/explosion/005.png",
        "images/explosion/006.png",
        "images/explosion/007.png",
        "images/explosion/008.png",
        "images/explosion/009.png",
    ],
}

SCREEN = DotDict(SCREEN)
BULLET = DotDict(BULLET)
SHIP = DotDict(SHIP)
ROCK = DotDict(ROCK)
ROCK.LARGE = DotDict(LARGE_ROCK)
ROCK.MEDIUM = DotDict(MEDIUM_ROCK)
ROCK.SMALL = DotDict(SMALL_ROCK)
EXPLOSION = DotDict(EXPLOSION)
