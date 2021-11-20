import arcade

from Point import Point
from config import EXPLOSION


class Explosion:
    def __init__(self, center: Point = Point(0, 0), size: int = EXPLOSION.SIZE):
        self._frame: int = 1
        self._delay: int = EXPLOSION.DELAY
        self._center: Point = center
        self._size: int = size
        self._is_alive: bool = True

    def draw(self):

        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            height=self.size * 2,
            width=self.size * 2,
            texture=arcade.load_texture(EXPLOSION.IMG[self.frame - 1]),
        )

    def advance(self):
        if self.delay == 1:
            self.delay = EXPLOSION.DELAY
            if self.frame < EXPLOSION.FRAMES:
                self.frame += 1
            else:
                self.is_alive = False
        else:
            self.delay -= 1

    @property
    def frame(self) -> int:
        return self._frame

    @frame.setter
    def frame(self, frame: int) -> None:
        self._frame = frame

    @property
    def delay(self) -> int:
        return self._delay

    @delay.setter
    def delay(self, delay: int) -> None:
        self._delay = delay

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, center: Point) -> None:
        self._center = center

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        self._size = size

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self._is_alive = is_alive
