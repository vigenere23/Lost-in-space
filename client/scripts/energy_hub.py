"""Contient la classe EnergyHub."""
import pyglet as pg


class EnergyHub(object):
    """S'occupe de l'affichage de la barre d'énergie du vaisseau.

    Paramètres
    ----------
    ship: Ship()
        vaisseau du joueur.

    begin_x, begin_y: int
        position du début de la barre d'énergie horizontale et verticale.

    width, height: int
        largeur et hauteur de la barre.
    """

    def __init__(self, ship, begin_x, begin_y, width, height):
        self.__ship = ship
        self.__starting_energy = ship.get_energy()
        self.__width = width
        self.__height = height
        self.__begin_x = begin_x
        self.__begin_y = begin_y

        self.__text = pg.text.Label(
            "Énergie",
            font_size=10,
            bold=True,
            x=5, y=682)

        self.__border = self.init_border()
        self.__bar = ()

        self.update()

    def init_border(self):
        """Créer les bordures de la barre.

        Retourne
        --------
        tuple
            Coordonnées des contours de la barre.
        """
        vert0 = (self.__begin_x, self.__begin_y)
        vert1 = (self.__begin_x, self.__begin_y + self.__height)
        vert2 = (self.__begin_x + self.__width, self.__begin_y + self.__height)
        vert3 = (self.__begin_x + self.__width, self.__begin_y)
        return (*vert0, *vert1, *vert2, *vert3)

    def update(self):
        """Met à jour la barre d'énergie."""
        length = int(
            self.__ship.get_energy() / self.__starting_energy * self.__width)

        vert0 = (self.__border[0], self.__border[1])
        vert1 = (self.__border[2], self.__border[3])
        vert2 = (self.__border[2] + length, self.__border[5])
        vert3 = (self.__border[0] + length, self.__border[7])
        self.__bar = (*vert0, *vert1, *vert2, *vert3)

    def draw(self):
        """Dessine la barre à l'écran.

        1. Appelle la fonction de mise-à-jour de la barre.
        2. Affiche le texte.
        3. Affiche le contour.
        4. Affiche la barre.
        """

        self.update()

        self.__text.draw()

        pg.graphics.draw_indexed(
            4, pg.gl.GL_LINES,
            [0, 1, 1, 2, 2, 3, 3, 0],
            ('v2i', self.__border)
        )

        pg.graphics.draw_indexed(
            4, pg.gl.GL_TRIANGLES,
            [0, 1, 2, 2, 3, 0],
            ('v2i', self.__bar)
        )
