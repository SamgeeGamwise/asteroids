import copy
from random import randint, choice
from typing import List

import arcade

from Point import Point
from Velocity import Velocity
from config import ROCK, SCREEN, SHIP
from rock.MediumRock import MediumRock
from rock.Rock import Rock
from rock.SmallRock import SmallRock


class LargeRock(Rock):
    def __init__(self) -> None:
        super().__init__(
            center=Point(
                choice([randint(0, (SCREEN.WIDTH / 2) - SHIP.RADIUS),
                        randint((SCREEN.WIDTH / 2) + SHIP.RADIUS, SCREEN.WIDTH)]),
                choice([randint(0, (SCREEN.HEIGHT / 2) - SHIP.RADIUS),
                        randint((SCREEN.HEIGHT / 2) + SHIP.RADIUS, SCREEN.HEIGHT)])),
            velocity=Velocity.angle_speed(randint(0, 360), ROCK.LARGE.SPEED),
            hit_box=ROCK.LARGE.RADIUS,
            spin=ROCK.LARGE.SPIN
        )

    def draw(self):
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            height=ROCK.LARGE.RADIUS,
            width=ROCK.LARGE.RADIUS,
            texture=arcade.load_texture(ROCK.LARGE.IMG),
            angle=self.angle
        )

    def destroy(self, rocks: List['Rock'], index: int) -> None:
        rocks.pop(index)
        rocks += [
            MediumRock(copy.copy(self.center), copy.copy(self.velocity) + Velocity(0, 2)),
            MediumRock(copy.copy(self.center), copy.copy(self.velocity) + Velocity(0, -2)),
            SmallRock(copy.copy(self.center), copy.copy(self.velocity) + Velocity(5, 0))
        ]

