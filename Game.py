"""
File: Game.py
Original Author: Br. Burton
Final Author: Samuel Krohn

Creates the Game class, initializes an instance of the game class, and runs the arcade library
"""

from typing import List

import arcade

from Explosion import Explosion
from FlyingObject import FlyingObject
from config import SCREEN, ROCK
from player.Ship import Ship
from rock.LargeRock import LargeRock
from rock.Rock import Rock


class Game(arcade.Window):
    """
    The Game class is used to initialize the Asteroid game. The arcade library should be ran after a
    Game instance is created to start the Asteroids game.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Constructs a new Game instance

        :param int width: Window width
        :param int height: Window height
        """

        super().__init__(width, height)
        self._held_keys: set[int] = set()
        self._ship: Ship = Ship()
        self._rocks: List[Rock] = [LargeRock() for _ in range(ROCK.INITIAL_ROCK_COUNT)]
        self._explosions: List[Explosion] = []

        arcade.set_background_color(SCREEN.COLOR)

    def on_draw(self) -> None:
        """
        on_draw handles all arcade rendering

        :return:
        """

        arcade.start_render()

        [bullet.draw() for bullet in self.ship.bullets]
        [rock.draw() for rock in self.rocks]
        [explosion.draw() for explosion in self.explosions]

        if self.ship.is_alive:
            self.ship.draw()
            if len(self.rocks) == 0:
                self.draw_win()
        elif not self.ship.is_alive:
            self.draw_game_over()

    def update(self, delta_time: float) -> None:
        """
        update progresses the game between each frame. It will identify keys pressed, move each FlyingObject,
        mirror FlyingObjects around the screen, and remove dead FlyingObjects. Lastly, it will check collisions.

        :param delta_time:
        :return:
        """

        # Check keys pressed
        self.check_keys()

        # Move ship and check if outside of range
        if self.ship.is_alive:
            self.ship.advance()
            Game.check_flip(self.ship)

        # Move bullets and check if outside of range or dead
        for index, bullet in enumerate(self.ship.bullets):
            bullet.advance()
            Game.check_flip(bullet)
            if not bullet.is_alive():
                self.explosions.append(Explosion(bullet.center, bullet.hit_box))
                self.ship.bullets.pop(index)

        # Advance explosion frames and check if animation is finished
        for index, explosion in enumerate(self.explosions):
            explosion.advance()
            if not explosion.is_alive:
                self.explosions.pop(index)

        # Move rocks and check if outside of range
        for index, rock in enumerate(self.rocks):
            rock.advance()
            Game.check_flip(rock)

        self.check_collision(self.rocks, self.ship.bullets)
        if self.ship.is_alive:
            self.check_collision([self.ship], self.rocks)

    def check_collision(self, group_1: List[FlyingObject], group_2: List[FlyingObject]):
        """
        takes two lists of FlyingObjects and compares their location and hit_box to determine if they have collided.
        Any collision has occurred, it will call the FlyingObject's destroy method and create an explosion at that
        point

        :param group_1:
        :param group_2:
        :return:
        """

        for index_1, flying_object_1 in enumerate(group_1):
            for index_2, flying_object_2 in enumerate(group_2):
                too_close: int = round((flying_object_1.hit_box / 2)) + round((flying_object_2.hit_box / 2))

                intersect_on_x: bool = abs(flying_object_1.center.x - flying_object_2.center.x) < too_close
                intersect_on_y: bool = abs(flying_object_1.center.y - flying_object_2.center.y) < too_close

                if intersect_on_x and intersect_on_y:
                    flying_object_1.destroy(group_1, index_1)
                    flying_object_2.destroy(group_2, index_2)
                    self.explosions.append(Explosion(flying_object_1.center, flying_object_1.hit_box))
                    break

    def check_keys(self) -> None:
        """
        Checks which keys are being held and calls necessary methods associated with key

        :return:
        """

        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()

        if arcade.key.UP in self.held_keys:
            self.ship.move_forward()

        if arcade.key.DOWN in self.held_keys:
            self.ship.move_backwards()

        # # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #     self.ship.fire()

    def on_key_press(self, key: int, modifiers: int) -> None:
        """
        Adds key being held to held_keys if the ship is still alive. If the key is the space bar, will immediately call
        the fire method

        :param key:
        :param modifiers:
        :return:
        """

        if self.ship.is_alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                self.ship.fire()

    def on_key_release(self, key: int, modifiers: int) -> None:
        """
        Checks for keys not being held to remove them from held_keys

        :param key:
        :param modifiers:
        :return:
        """

        if key in self.held_keys:
            self.held_keys.remove(key)

    @property
    def held_keys(self) -> set[int]:
        """
        getter for held_keys property

        :returns: a set of key id values
        :type: set[int]
        """

        return self._held_keys

    @property
    def ship(self) -> Ship:
        """
        getter for ship property

        :type: Ship
        """

        return self._ship

    @property
    def explosions(self) -> List[Explosion]:
        """
        getter for explosions property

        :type: List[Explosion]
        """

        return self._explosions

    @property
    def rocks(self) -> List[Rock]:
        """
        getter for rocks property

        :type: List[Rock]
        """

        return self._rocks

    @rocks.setter
    def rocks(self, rocks: List[Rock]):
        """
        setter for rocks property

        :param rocks:
        :return:
        """

        self._rocks = rocks

    @staticmethod
    def check_flip(flying_object: FlyingObject):
        """
        checks if a flying object needs to be flipped horizontally/vertically and flips as needed

        :param flying_object:
        :return:
        """

        flying_object.check_flip_horizontal(SCREEN.HEIGHT)
        flying_object.check_flip_vertical(SCREEN.WIDTH)

    @staticmethod
    def draw_game_over():
        """
        draws 'Game Over' on screen in red

        :return:
        """

        start_x = SCREEN.WIDTH / 2 - 80
        start_y = SCREEN.HEIGHT - 300
        arcade.draw_text(
            text="Game Over",
            start_x=start_x,
            start_y=start_y,
            font_size=28,
            color=arcade.color.RED
        )

    @staticmethod
    def draw_win():
        """
        draws 'Win!' on screen in green

        :return:
        """

        start_x = SCREEN.WIDTH / 2 - 50
        start_y = SCREEN.HEIGHT - 250
        arcade.draw_text(
            text="Win!",
            start_x=start_x,
            start_y=start_y,
            font_size=28,
            color=arcade.color.GREEN
        )


# Creates the game and starts it going
window = Game(SCREEN.WIDTH, SCREEN.HEIGHT)
arcade.run()
