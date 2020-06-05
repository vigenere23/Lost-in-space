"""Définition de la classe Ship."""

import math

from common.vec2 import Vec2
from .ship import Ship
from .energy_hub import EnergyHub


class PlayerShip(Ship):
    """
    Parameters
    ----------
    image_path : string
        path to image of the ship to use

    x, y : float (pixels)
        Positions horizontales et verticales initiales du vaisseau.

    accel : float (pixels/s^2)
        Accélération du vaisseau.

    energy : float (seconds)
        Energy of the ship (in seconds of up-arrow pressing).

    ang_velocity : float (°/s)
        Angular velocity (fixed) when rotating.

    bounciness : float (%) [0, 1]
        1 for full bounce, 0 for no bounce.
    """

    def __init__(self,
                 username,
                 image_path,
                 x, y,
                 accel=100,
                 energy=30,
                 ang_velocity=180,
                 bounciness=0.9):

        super().__init__(username, image_path, x, y)

        self.__accel = accel
        self.__energy = energy
        self.__ang_velocity = ang_velocity
        self.__bounciness = bounciness

        self.__energy_hub = EnergyHub(self, 62, 681, 70, 10)

    def get_position(self):
        return Vec2(self.x, self.y)

    def get_velocity(self):
        return self._velocity

    def get_speed(self):
        return self._velocity.norm()

    def get_rotation(self):
        return -self.rotation

    def get_energy(self):
        return self.__energy

    def get_status(self):
        return (
            tuple(self.get_position()),
            tuple(self.get_velocity()),
            int(self.get_rotation())
        )

    def update_rotation(self, detla_time, clockwise=True):
        if clockwise:
            self.rotation += self.__ang_velocity * detla_time
        else:
            self.rotation -= self.__ang_velocity * detla_time

    def update_velocity(self, delta_time):
        if self.__energy > 0:
            delta_vitesse = self.__accel*delta_time
            angle = math.radians(self.get_rotation())
            self._velocity.x += delta_vitesse * math.cos(angle)
            self._velocity.y += delta_vitesse * math.sin(angle)
            self.__energy -= delta_time

        elif self.__energy < 0:
            self.__energy = 0

    def bounce(self, normal_vec, incidence_vec):
        """Updates ship speed after a bounce

        Parameters
        ----------
        normal_vec : Vec2
            Vector normal to the bouncing surface

        incidence_vec : Vec2
            Reflected vector of the ship (according to `normal_vec`)
        """
        reflected_vec = incidence_vec - 2 * (
            incidence_vec.dot_product(normal_vec)) * normal_vec
        new_velocity = (
            self.__bounciness *
            self.get_velocity().norm() *
            reflected_vec.normalize())

        self.set_velocity(new_velocity)

    def set_status(self, position, velocity, angle):
        pass

    def draw(self):
        super().draw()
        self.__energy_hub.draw()
