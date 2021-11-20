import copy
from typing import List

import arcade

from Point import Point
from Velocity import Velocity
from config import ROCK
from rock.Rock import Rock
from rock.SmallRock import SmallRock


class MediumRock(Rock):
    def __init__(self, center: Point, velocity: Velocity) -> None:
        super().__init__(
            center=center,
            velocity=velocity,
            hit_box=ROCK.MEDIUM.RADIUS,
            spin=ROCK.MEDIUM.SPIN
        )

    def draw(self):
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            height=ROCK.MEDIUM.RADIUS,
            width=ROCK.MEDIUM.RADIUS,
            texture=arcade.load_texture(ROCK.MEDIUM.IMG),
            angle=self.angle
        )

    def destroy(self, rocks: List['Rock'], index: int) -> None:
        rocks.pop(index)
        rocks += [
            SmallRock(copy.copy(self.center), copy.copy(self.velocity) + Velocity(1.5, 1.5)),
            SmallRock(copy.copy(self.center), copy.copy(self.velocity) + Velocity(-1.5, -1.5))
        ]

