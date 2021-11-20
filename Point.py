class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self._x: float = x
        self._y: float = y

    def advance(self, dx: float, dy: float) -> None:
        self._x = self._x + dx
        self._y = self._y + dy

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float) -> None:
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float) -> None:
        self._y = y

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)
