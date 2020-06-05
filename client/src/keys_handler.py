import pyglet as pg


class KeysHandler(pg.window.key.KeyStateHandler):
    def keys_pressed(self):
        """Check if a key is pressed."""
        key_is_pressed = False
        for pressed_key in self.values():
            if pressed_key:
                key_is_pressed = True
                break
        return key_is_pressed
