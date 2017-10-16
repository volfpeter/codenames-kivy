from kivy.lang.builder import Builder
from kivy.properties import ListProperty
from kivy.uix.widget import Widget

Builder.load_file("RectangleWidget.kv")


class RectangleWidget(Widget):
    """
    A single rectangle in the table.
    """

    color = ListProperty()

    def __init__(self, **kwargs):
        super(RectangleWidget, self).__init__(**kwargs)

        self.color = (0.5, 0.5, 0.5, 1)
