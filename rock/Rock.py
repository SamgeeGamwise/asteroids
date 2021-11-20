from typing import List

from FlyingObject import FlyingObject
from Point import Point
from Velocity import Velocity


class Rock(FlyingObject):
    def __init__(
            self,
            center: Point = Point(0, 0),
            velocity: Velocity = Velocity(0, 0),
            hit_box: int = 0,
            spin: int = 0,
            angle: int = 0
    ) -> None:
        super().__init__(center=center, velocity=velocity, hit_box=hit_box)
        self.angle: int = angle
        self.spin: int = spin

    def advance(self) -> None:
        super().advance()
        self.angle += self.spin

    def draw(self):
        pass

    def destroy(self, rocks: List['Rock'], index: int) -> None:
        rocks.pop(index)
        rocks += []
