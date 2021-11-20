import math


class Velocity:
    def __init__(self, dx: float = 0, dy: float = 0) -> None:
        self._dx: float = dx
        self._dy: float = dy

    def __add__(self, other: 'Velocity'):
        new_velocity: Velocity = Velocity(self.dx + other.dx, self.dy + other.dy)
        return new_velocity

    @staticmethod
    def angle_speed(angle: float, speed: int) -> 'Velocity':
        radians: float = (angle * math.pi) / 180
        dx = speed * math.sin(radians)
        dy = speed * math.cos(radians)
        return Velocity(dx, dy)

    @property
    def dx(self) -> float:
        return self._dx

    @dx.setter
    def dx(self, dx: float) -> None:
        self._dx = dx

    @property
    def dy(self) -> float:
        return self._dy

    @dy.setter
    def dy(self, dy: float) -> None:
        self._dy = dy
