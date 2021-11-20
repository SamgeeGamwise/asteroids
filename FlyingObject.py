from typing import List

import abc
from Point import Point
from Velocity import Velocity


class FlyingObject:
    def __init__(self, center: Point = Point(0, 0), velocity: Velocity = Velocity(0, 0), hit_box: int = 0) -> None:
        self._center: Point = center
        self._velocity: Velocity = velocity
        self._hit_box: int = hit_box

    def advance(self) -> None:
        self.center.advance(self.velocity.dx, self.velocity.dy)

    def check_flip_horizontal(self, height: int) -> None:
        if self.center.y > height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = height

    def check_flip_vertical(self, width: int) -> None:
        if self.center.x > width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = width

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, center: Point) -> None:
        self._center = center

    @property
    def velocity(self) -> Velocity:
        return self._velocity

    @velocity.setter
    def velocity(self, velocity: Velocity) -> None:
        self._velocity = velocity

    @property
    def hit_box(self) -> int:
        return self._hit_box

    @hit_box.setter
    def hit_box(self, hit_box: int) -> None:
        self._hit_box = hit_box

    @abc.abstractmethod
    def destroy(self, flying_objects: List['FlyingObject'], index: int) -> None:
        pass

    @abc.abstractmethod
    def draw(self):
        pass
