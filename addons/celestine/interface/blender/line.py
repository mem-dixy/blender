from celestine.window.line import Line as master
from celestine.window.collection import Rectangle

from . import package
from .button import Button
from .image import Image
from .label import Label

from .container import Container


class Line(Container):
    def action(self):
        pass

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()
            for child in self.children():
                child.select(cord_x, cord_y)

    def button(self, tag, text, action):
        return self.item_set(
            tag,
            Button(
                self.collection,
                text,
                lambda: self.turn(action),
                self.spawn(),
            ),
        )

    def image(self, tag, image):
        return self.item_set(
            tag,
            Image(
                self.collection,
                image,
                self.spawn(),
            ),
        )

    def label(self, tag, text):
        return self.item_set(
            tag,
            Label(
                self.collection,
                text,
                self.spawn(),
            ),
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, page, tag, rectangle):
        super().__init__(page, tag, rectangle, 10, 0)
