from .package import mesh as _mesh


class Widget():
    def __init__(self, rectangle):
        self.cord_x_min = rectangle.cord_x_min
        self.cord_y_min = rectangle.cord_y_min
        self.cord_x_max = rectangle.cord_x_max
        self.cord_y_max = rectangle.cord_y_max

    def inside(self, cord_x, cord_y):
        aaa = self.cord_x_min < cord_x
        bbb = self.cord_y_min < cord_y
        ccc = self.cord_x_max > cord_x
        ddd = self.cord_y_max > cord_y
        return aaa and bbb and ccc and ddd

    def action(self):
        pass

    def draw(self, mesh):
        mesh.location = (self.cord_x_min, self.cord_y_min, 0)

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()
