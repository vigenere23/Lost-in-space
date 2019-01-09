"""Classe de vecteurs 2D."""

import math


class Vec2(object):
    """Vecteur 2D comportant plusieurs méthodes de calculs.

    Paramètres
    ----------
    vec_x, vec_y : float
        Composantes vectorielles initiales horizontale et verticale.
    """

    def __init__(self, vec_x=0, vec_y=0):
        self.x, self.y = vec_x, vec_y

    @classmethod
    def from_list(cls, vec_list):
        if len(vec_list) != 2:
            raise ValueError("The list must have a lenght of 2")
        return cls(vec_list[0], vec_list[1])

    def __str__(self):
        """Affiche un tuple de la forme (x, y)."""
        return str(tuple(self))

    def __eq__(self, other):
        """Défini l'égalité entre deux vecteurs.

        Deux vecteurs sont égaux si leurs composantes x ET y sont égales.
        """
        if self.x == other.x and self.y == other.y:
            return True
        return False

    @classmethod
    def dist(cls, vec1, vec2):
        if not isinstance(vec1, Vec2) or not isinstance(vec2, Vec2):
            raise ValueError("vecs must be of type Vec2")
        
        delta_vec = vec2 - vec1
        return delta_vec.norm()

    def __gt__(self, other):
        """Définition du plus grand.

        Retourne vrai si au moins une des composantes est plus grande.
        """
        if self.x > other.x or self.y > other.y:
            return True
        return False

    def __lt__(self, other):
        """Définition du plus petit.

        Retourne vrai si au moins une des composantes est plus petite.
        """
        if self.x < other.x or self.y < other.y:
            return True
        return False

    def __ge__(self, other):
        """Définition du plus grand ou égal.

        Retourne vrai si toutes les composantes sont plus grandes ou égales.
        """
        if self.x >= other.x and self.y >= other.y:
            return True
        return False

    def __le__(self, other):
        """Définition du plus petit ou égal.

        Retourne vrai si toutes les composantes sont plus petites ou égales.
        """
        if self.x <= other.x and self.y <= other.y:
            return True
        return False

    def __add__(self, other):
        """Ajout de deux vecteurs."""
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Soustraction de deux vecteurs."""
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Opération de multiplication.

        Si 'other' est un vecteur, retourne le produit croisé (x).
        Si 'other' est un scalaire, retourne la multiplication scalaire.
        """
        if isinstance(other, type(self)):
            return self.x * other.y - self.y * other.x
        elif isinstance(other, (float, int)):
            return Vec2(other * self.x, other * self.y)
        else:
            raise TypeError(
                "Vec2() ne peut être multiplié par {}".format(type(other))
            )

    def __rmul__(self, other):
        """Permet la multiplication à droite ( ex.: 4 * Vec2() )."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Division par un scalaire."""
        if isinstance(other, (float, int)):
            return Vec2(self.x / other, self.y / other)
        else:
            raise TypeError(
                "Vec2() ne peut être divisé par {}".format(type(other))
            )

    def __iter__(self):
        """Retourne le vecteur en temps que tuple standard."""
        yield self.x
        yield self.y

    def normal(self):
        """Trouve vecteur à 90° de self."""
        return Vec2(-self.y, self.x)

    def normalize(self):
        """Transforme le vecteur en vecteur unitaire."""
        return self / self.norm()

    def angle(self):
        """Calcule l'angle du vecteur."""
        return math.atan2(self.y, self.x)

    def norm(self):
        """Retourne la norme du vecteur (float)."""
        return math.sqrt(self.x**2 + self.y**2)

    def dot_product(self, other):
        """Calcule le produit scalaire de deux vecteurs."""
        return self.x * other.x + self.y * other.y
