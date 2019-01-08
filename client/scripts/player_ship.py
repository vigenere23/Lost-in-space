"""Définition de la classe Ship."""

import math

from .ship import Ship
from .energy_hub import EnergyHub
from .vec2 import Vec2


class PlayerShip(Ship):
    """Vaisseau local du jeu.

    Paramètres
    ----------
    image_path : string
        Chemin d'accès à l'image du vaisseau.

    x, y : float (pixels)
        Positions horizontales et verticales initiales du vaisseau.

    accel : float (pixels/s^2)
        Accélération du vaisseau.

    energy : float (secondes)
        Énergie du vaisseau en temps d'appui de la touche ↑.

    ang_velocity : float (°/s)
        Vitesse angulaire du vaisseau (vitesse de rotation).

    bounciness : float (%) [0, 1]
        Coefficient de rebond. 1 signifie aucune perte de vitesse lors d'une
        collision.
    """

    def __init__(self,
                 username,
                 image_path,
                 x, y,
                 accel, energy, ang_velocity, bounciness):

        super().__init__(username, image_path, x, y)

        self.__accel = accel
        self.__energy = energy
        self.__ang_velocity = ang_velocity
        self.__bounciness = bounciness

        self.__energy_hub = EnergyHub(self, 62, 681, 70, 10)

    def get_position(self):
        """Obtenir la position de x et y en même temps.

        Retourne
        --------
        Vec2
            Position actuelle du vaisseau x et y (pixels).
        """
        return Vec2(self.x, self.y)

    def get_velocity(self):
        """Retourne le vecteur vitesse.

        À ne pas confondre avec get_speed, qui retourne la NORME de vitesse.

        Retourne
        --------
        Vec2
            Vélocité en temps que Vec2.
        """
        return self._velocity

    def get_speed(self):
        """Retourne la norme de la vitesse actuelle du vaisseau."""
        return self._velocity.norm()

    def get_rotation(self):
        """Retourne l'angle universel de rotation du sprite."""
        return -self.rotation

    def get_energy(self):
        """Retourne l'énergie restante du vaisseau."""
        return self.__energy

    def get_status(self):
        """Retourne l'état général du vaisseau.

        Retourne
        --------
        tuple of tuples (position(x, y), vitesse(x, y), angle)
        """
        return (
            tuple(self.get_position()),
            tuple(self.get_velocity()),
            int(self.get_rotation())
        )

    def update_rotation(self, detla_time, *, clockwise=True):
        """Met à jour la rotation du vaisseau.

        Paramètres
        ----------
        clockwise : bool
            Sens de rotation du vaisseau (True étant horaire).
        """
        if clockwise:
            self.rotation += self.__ang_velocity * detla_time
        else:
            self.rotation -= self.__ang_velocity * detla_time

    def update_velocity(self, delta_time):
        """Met à jour le vecteur vitesse du vaisseau.

        Redéfini les vitesses x et y en fonction de l'angle actuel.
        Appelé lors de la propulsion.
        """
        if self.__energy > 0:
            delta_vitesse = self.__accel*delta_time
            angle = math.radians(self.get_rotation())
            self._velocity.x += delta_vitesse * math.cos(angle)
            self._velocity.y += delta_vitesse * math.sin(angle)
            self.__energy -= delta_time

        elif self.__energy < 0:
            self.__energy = 0

    def bounce(self, normal_vec, incidence_vec):
        """Calcule la nouvelle vitesse du vaisseau après rebond.

        Paramètres
        ----------
        normal_vec : Vec2
            Vecteur normal à la surface de collision.

        incidence_vec : Vec2
            Vecteur de rebond (selon réflexion par rapport à nomral_vec).
        """
        reflected_vec = incidence_vec - 2 * (
            incidence_vec.dot_product(normal_vec)) * normal_vec
        new_velocity = (
            self.__bounciness *
            self.get_velocity().norm() *
            reflected_vec.normalize())

        self.set_velocity(new_velocity)

    def set_status(self, position, velocity, angle):
        """Met à jour les attributs du vaisseau.

        Seulement pour la classe parente.
        """
        pass

    def draw(self):
        """Regroupe les fonctions de dessin."""
        super().draw()
        self.__energy_hub.draw()
