from typing import List

import arcade

from Point import Point
from Velocity import Velocity
from config import ROCK
from rock.Rock import Rock


class SmallRock(Rock):
    def __init__(self, center: Point, velocity: Velocity) -> None:
        super().__init__(
            center=center,
            velocity=velocity,
            hit_box=ROCK.SMALL.RADIUS,
            spin=ROCK.SMALL.SPIN
        )

    def draw(self):
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            height=ROCK.SMALL.RADIUS,
            width=ROCK.SMALL.RADIUS,
            texture=arcade.load_texture(ROCK.SMALL.IMG),
            angle=self.angle
        )

    def destroy(self, rocks: List['Rock'], index: int) -> None:
        rocks.pop(index)
        rocks += []

