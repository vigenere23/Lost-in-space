"""Contient la classe Win()."""

import pyglet as pg


class WinHandler(object):
    """Permet de gérer la fenêtre lorsque quelqu'un gagne."""

    def __init__(self, window_width, window_height, keys):
        self.__winner = ""
        self.__keys = keys
        self.__pos_x = window_width // 2
        self.__pos_y = window_height // 2
        self.__win_text = None  # pyglet.text.Label()
        self.__press_any_keys_text = None  # pyglet.text.Label()

    def set_winner(self, winner):
        """Annonce un gagnant."""
        if self.__winner != "":
            raise TypeError("Un gagnant a déjà été annoncé!")

        self.__winner = winner
        self.__keys.clear()
        self.create_text()

    def has_winner(self):
        """Vérifie si un gagnant a été annoncé."""
        if self.__winner != "":
            return True
        return False

    def create_text(self):
        """Créer le texte à afficher."""
        self.__win_text = pg.text.Label(
            "{} a gagné la partie!".format(self.__winner),
            font_size=28,
            bold=True,
            anchor_x='center',
            anchor_y='center',
            x=self.__pos_x,
            y=self.__pos_y + 20)

        self.__press_any_keys_text = pg.text.Label(
            "(Appuyez sur n'importe quelle touche pour fermer...)",
            font_size=12,
            anchor_x='center',
            anchor_y='center',
            x=self.__pos_x,
            y=self.__pos_y - 20)

    def draw(self):
        """Affiche les textes à l'écran."""
        self.__win_text.draw()
        self.__press_any_keys_text.draw()
