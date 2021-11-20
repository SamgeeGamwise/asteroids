from typing import List

import arcade

from FlyingObject import FlyingObject
from Point import Point
from Velocity import Velocity
from config import SHIP, SCREEN
from player.Bullet import Bullet


class Ship(FlyingObject):
    def __init__(self) -> None:
        super().__init__(
            center=Point(SCREEN.WIDTH / 2, SCREEN.HEIGHT / 2),
            hit_box=SHIP.RADIUS
        )
        self._bullets: List[Bullet] = []
        self._angle: float = 0.0
        self._is_alive: bool = True

    def draw(self) -> None:
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            height=SHIP.RADIUS,
            width=SHIP.RADIUS,
            texture=arcade.load_texture(SHIP.IMG),
            angle=-self.angle,
        )

    def destroy(self, ships: List['Ship'], index: int) -> None:
        ships[index].is_alive = False

    def move_forward(self) -> None:
        self.velocity += Velocity.angle_speed(self._angle, SHIP.THRUST_AMOUNT)

    def move_backwards(self):
        self.velocity += Velocity.angle_speed(self._angle, -SHIP.THRUST_AMOUNT)

    def rotate_left(self) -> None:
        self.angle -= SHIP.TURN_AMOUNT

    def rotate_right(self) -> None:
        self.angle += SHIP.TURN_AMOUNT

    def fire(self) -> None:
        bullet: Bullet = Bullet(self.center, self.velocity, self.angle)
        self.bullets.append(bullet)

    @property
    def bullets(self) -> List[Bullet]:
        return self._bullets

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        self._angle = angle

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool):
        self._is_alive = is_alive

