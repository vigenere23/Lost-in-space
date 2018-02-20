"""Classe permettant les manipulations reliées aux obstacles."""

import pyglet as pg

import scripts.polytri as polytri
from scripts.vec2 import Vec2


class Map(object):
    """Classe de gestion des obstacles (la 'map').

    Permet de générer une liste d'obstacles optimisé pour le rendement.

    Paramètres
    ----------
    obstacles : list of list of list (coordonnée 2D)
        Liste des sommets de chaque polygone à afficher en temps qu'obstacles.

    end_point : list (coordonnée 2D)
        Point d'arrivée des vaisseaux.

    Attributs
    ---------
    __polygons : list of list of list (coords)
        Coordonnées des obstacles (polygones), incluant les limites.

    __verticies_coords : list
        Coordonnées (applaties) des sommets uniques des triangles à générer.

    __verticies_indexes : list
        Index, en ordre, des sommets à générer.

    __verticies_number : int
        Nombre de sommets à afficher (pour pyglet.gl.GL_TRIANGLES())

    __colors : list
        Liste de couleurs (applatie) des obstacles.

    __edge_vectors : list of tuples
        Groupement (sommet, vecteur) permettant de représenter les arrêtes des
        polygones.

    __end_point : pyglet.Sprite
        Image affichée au point d'arrivée.
    """

    def __init__(self, obstacles, end_point):
        self.__polygons = obstacles
        self.__verticies_coords = ()
        self.__verticies_indexes = []
        self.__verticies_number = 0
        self.__colors = ()
        self.__edge_vectors = []
        self.__end_point = self.init_end_point(end_point)  # pg.sprite.Sprite()

        self.__add_boundaries()
        self.__generate()

    def __add_boundaries(self):
        """Créer une limite de jeu aux bords de la fenêtre."""
        # gauche
        self.__polygons.append(create_rectangle((-1, 0), (0, 700)))
        # bas
        self.__polygons.append(create_rectangle((0, -1), (700, 0)))
        # droite
        self.__polygons.append(create_rectangle((700, 0), (701, 700)))
        # haut
        self.__polygons.append(create_rectangle((0, 700), (700, 701)))

    def __generate(self):
        """Prépare et génère les listes d'obstacles de façon optimisée.

        1. Créer une liste des sommets et arrêtes externes pour la collision.
        2. Transforme les polygones en triangles.
        3. Créer une liste de sommets unique, une liste d'indices et une liste
           de couleurs pour le rendement OpenGL.
        """
        verticies = []
        new_index = 0

        for polygon in self.__polygons:
            # Créer la liste de tuples (sommet, arrete) pour les collisions.
            size = len(polygon)
            for i, vertex in enumerate(polygon):
                vertex = Vec2(*vertex)
                self.__edge_vectors.append(
                    (vertex, Vec2(*polygon[(i + 1) % size]) - vertex)
                )
            # Créer la liste de sommets et arrêtes unique des triangles.
            for triangle in polytri.triangulate(polygon):
                for vertex in triangle:
                    try:
                        index = verticies.index(vertex)
                    except BaseException:
                        verticies.append(vertex)
                        self.__verticies_indexes.append(new_index)
                        new_index += 1
                    else:
                        self.__verticies_indexes.append(index)

        self.__verticies_number = len(verticies)
        self.__verticies_coords = tuple(
            coord for vertex in verticies for coord in vertex
        )
        self.__colors = (60, 64, 78) * self.__verticies_number

    def init_end_point(self, end_point_coords):
        """Créé l'image à la position finale."""
        image = pg.image.load("./images/death-star.png")
        image.anchor_x = image.width // 2  # Doit être entier
        image.anchor_y = image.height // 2
        end_point = pg.sprite.Sprite(image, *end_point_coords)
        end_point.scale = 0.4
        return end_point

    def check_collision(self, delta_time, ship):
        """Vérifie s'il y a une collision avec le vaisseau.

        Paramètres
        ----------
        ship : Ship
            Vaisseau pour lequel on teste la collisions.

        delta_time : float (secondes)
            Permet de pondérer le vecteur delta_p.
        """
        pos_p = ship.get_position()
        delta_p = ship.get_velocity() * delta_time
        for vertex_q, delta_q in self.__edge_vectors:
            denum = delta_p * delta_q
            if denum != 0:
                frac = (vertex_q - pos_p) / denum
                coeff_r = frac * delta_q
                coeff_s = frac * delta_p
                if (0 <= coeff_r <= 1) and (0 <= coeff_s <= 1):
                    normal = delta_q.normal().normalize()
                    ship.bounce(normal, delta_p)
                    self.check_collision(delta_time, ship)

    def draw(self):
        """Dessine les obstacles ainsi que le point final."""
        pg.graphics.draw_indexed(
            self.__verticies_number,
            pg.gl.GL_TRIANGLES,
            self.__verticies_indexes,
            ('v2i', self.__verticies_coords),
            ('c3B', self.__colors)
        )
        self.__end_point.draw()


def create_rectangle(start, end):
    """Génère les sommets d'un rectangle.

    Paramètres
    ----------
    start : tuple (coordonnée 2D)
        Coin quelconque.

    end : tuple (coordonnée 2D)
        Coin opposé (en diagonale) à 'start'.

    Retourne
    --------
    tuple of tuples (coordonnée 2D)
        Liste des sommets du rectangle.
    """
    if len(start) != 2 or len(end) != 2:
        raise ValueError("Les coordonnées doivent être de taille 2!")
    min_x, min_y = start
    max_x, max_y = end

    vert1 = (min_x, min_y)
    vert2 = (max_x, min_y)
    vert3 = (max_x, max_y)
    vert4 = (min_x, max_y)

    return (vert1, vert2, vert3, vert4)
