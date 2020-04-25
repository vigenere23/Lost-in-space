import pyglet as pg


class WinHandler(object):
    def __init__(self, window_width, window_height, keys):
        self.__winner = None
        self.__keys = keys
        self.__pos_x = window_width // 2
        self.__pos_y = window_height // 2
        self.__win_text = None  # pyglet.text.Label()
        self.__press_any_keys_text = None  # pyglet.text.Label()

    def set_winner(self, winner):
        self.__winner = winner
        self.__keys.clear()
        self.create_text()

    def create_text(self):
        self.__win_text = pg.text.Label(
            "{} won the game!".format(self.__winner),
            font_size=28,
            bold=True,
            anchor_x='center',
            anchor_y='center',
            x=self.__pos_x,
            y=self.__pos_y + 20)

        self.__press_any_keys_text = pg.text.Label(
            "(Press ENTER to close...)",
            font_size=12,
            anchor_x='center',
            anchor_y='center',
            x=self.__pos_x,
            y=self.__pos_y - 20)

    def draw(self):
        self.__win_text.draw()
        self.__press_any_keys_text.draw()
