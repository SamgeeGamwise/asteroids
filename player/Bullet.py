from typing import List

import arcade

from FlyingObject import FlyingObject
from Point import Point
from Velocity import Velocity
from config import BULLET


class Bullet(FlyingObject):
    def __init__(self, center: Point, velocity: Velocity, angle: float) -> None:
        bullet_center: Point = Point(center.x, center.y)
        bullet_velocity: Velocity = Velocity(velocity.dx, velocity.dy)
        super().__init__(center=bullet_center, velocity=bullet_velocity, hit_box=BULLET.RADIUS)
        self._angle: float = -angle - 90
        self._life: int = BULLET.LIFE
        self.velocity += Velocity.angle_speed(angle, BULLET.SPEED)

    def draw(self) -> None:
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            height=BULLET.HEIGHT,
            width=BULLET.WIDTH,
            texture=arcade.load_texture(BULLET.IMG),
            angle=self.angle + 90,
        )

    def advance(self) -> None:
        super().advance()
        self.life -= 1

    def is_alive(self) -> bool:
        return self.life > 0

    def destroy(self, bullets: List['Bullet'], index: int) -> None:
        bullets.pop(index)

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle: float) -> None:
        self._angle = angle

    @property
    def life(self) -> int:
        return self._life

    @life.setter
    def life(self, life: int) -> None:
        self._life = life
