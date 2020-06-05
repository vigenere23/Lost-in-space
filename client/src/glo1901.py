import json
import socket
import time

__auteur__ = "Marc Parizeau"
__date__ = "2017-09-04"


class Chrono:
    """Chronograph class."""

    def __init__(self, autostart=False):
        """Initialize counter to zero; if autostart true, start counting."""
        self.time = 0
        if autostart:
            self.last = time.perf_counter()
        else:
            self.last = None

    def get(self):
        """Get elapsed time since start; return 0 if not started."""
        current = time.perf_counter()
        if self.last:
            self.time += current - self.last
            self.last = current
        return self.time

    def reset(self, autostop=False):
        """Reset counter to zero; if autostop false, keep counting."""
        self.time = 0
        if autostop:
            self.last = None
        elif self.last:
            self.last = time.perf_counter()

    def start(self):
        """Start chronograph; does nothing if not already stoped."""
        if not self.last:
            self.last = time.perf_counter()
        return self

    def stop(self):
        """Stop chronograph; does nothing if already stopped."""
        if self.last:
            self.time += time.perf_counter() - self.last
            self.last = None


def testloop(chrono):
    """Tester l'interface de la classe Chrono."""
    commande = None
    while commande != 'quit':
        commande = input()
        if commande == 'start':
            chrono.start()
        elif commande == 'stop':
            chrono.stop()
        elif commande == 'reset':
            chrono.reset()
        elif commande == 'get':
            chrono.get()

        print('chrono={} sec'.format(chrono.get()))


if __name__ == '__main__':
    testloop(Chrono())
