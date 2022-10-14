from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact (Actor):

    def __init__(self):
        super (). __init__ ()
        self._message = ''
        self._points = 0

    def set_message(self,message):
        self._message = message
   
    def get_message(self):
        return self._message

    def get_points(self):
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._points = -1

        return self._points
    