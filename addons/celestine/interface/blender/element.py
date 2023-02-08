""""""

from celestine.window.collection import Box


class Element(Box):
    """"""

    def draw(self):
        """"""
        (x_dot, y_dot) = self.center_float()
        # child sets mesh and then calls this
        self.mesh.location = (x_dot, y_dot, 0)

    def poke(self, x_dot, y_dot):
        """"""
        return self.inside(x_dot, y_dot)
