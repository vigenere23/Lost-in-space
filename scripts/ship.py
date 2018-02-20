"""Définition de la classe Ship."""
import pyglet as pg

from scripts.vec2 import Vec2


class Ship(pg.sprite.Sprite):
    """Vaisseau local du jeu.

    Paramètres
    ----------
    image_path : string
        Chemin d'accès à l'image du vaisseau.

    x, y : float (pixels)
        Position horizontale et verticale initiale du vaisseau.
    """

    def __init__(self, pseudo, image_path, x, y):

        image = pg.image.load(image_path)
        image.anchor_x = image.width // 2  # Doit être entier
        image.anchor_y = image.height // 2
        super().__init__(image, x, y)

        self.rotation = -90
        self.scale = 0.25
        self._velocity = Vec2()
        if len(pseudo) > 10:
            pseudo = pseudo[:10] + "..."
        self.label = pg.text.Label(pseudo,
                                   font_size=10,
                                   bold=True,
                                   anchor_x='center',
                                   anchor_y='center')

    def translate(self, detla_time):
        """Incrémente les coordonnées du vaisseau."""
        new_x = self.x + self._velocity.x * detla_time
        new_y = self.y + self._velocity.y * detla_time
        self.set_position(new_x, new_y)

    def set_velocity(self, new_velocity):
        """Permet de modifier le vecteur vitesse."""
        assert isinstance(new_velocity, Vec2)
        self._velocity = new_velocity

    def set_status(self, position, velocity, angle):
        """Met à jour les attributs du vaisseau."""
        self.set_position(*position)
        self._velocity = Vec2(*velocity)
        self.rotation = -angle
        self.update_label()

    def disappear(self):
        """Fait 'disparaître' le vaisseau."""
        self.set_status([-100, -100], [0, 0], 0)

    def update_label(self):
        """Change la position du nom du joueur."""
        self.label.x = int(self.x)
        self.label.y = int(self.y) + 30

    def update(self, detla_time):
        """Met à jour les attributs du vaisseau et fait des vérifications.

        À NOTER : la rotation est mise-à-jour directement par GameWindow().

        Appelée toutes les 'detla_time' secondes.
        """
        self.translate(detla_time)
        self.update_label()

    def draw(self):
        """Affiche le vaisseau et le nom du joueur."""
        super().draw()
        self.label.draw()
