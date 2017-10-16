import random

from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.utils import rgba

from rectanglewidget import RectangleWidget

Builder.load_file("CodenamesTableWidget.kv")


class CodenamesTableWidget(GridLayout):
    """
    Table widget implementation.

    See `CodenamesTableWidget.kv`.
    """

    _MATERIAL_RED = rgba("#F44336")
    _MATERIAL_DARK_ORANGE = rgba("#FF5722")

    _MATERIAL_TEAL = rgba("#009688")
    _MATERIAL_GREEN = rgba("#4CAF50")
    _MATERIAL_LIGHT_GREEN = rgba("#8BC34A")

    _MATERIAL_INDIGO = rgba("#3F51B5")
    _MATERIAL_BLUE = rgba("#2196F3")
    _MATERIAL_LIGHT_BLUE = rgba("#03A9F4")

    _MATERIAL_BROWN = rgba("#795548")

    _MATERIAL_GREY = rgba("#9E9E9E")
    _MATERIAL_DARK_GREY = rgba("#424242")
    _MATERIAL_BLUE_GREY = rgba("#607D8B")
    _MATERIAL_DARK_BLUE_GREY = rgba("#37474F")

    ASSASSIN = _MATERIAL_DARK_BLUE_GREY
    BLUE = _MATERIAL_INDIGO
    RED = _MATERIAL_RED
    PASSER_BY = _MATERIAL_LIGHT_GREEN

    background_color = ObjectProperty((1, 1, 1, 1))

    def __init__(self, **kwargs):
        super(CodenamesTableWidget, self).__init__(**kwargs)

        # Set the default properties of the grid.
        self.cols = 5
        self.padding = "12dp"
        self.spacing = "3dp"

        # Add the rectangles.
        self._rectangles = []
        for i in range(25):
            rect = RectangleWidget()
            self.add_widget(rect)
            self._rectangles.append(rect)

        # Randomize the table.
        self.randomize()

    def randomize(self):
        starting_team =\
            CodenamesTableWidget.RED if random.random() < 0.5 else CodenamesTableWidget.BLUE
        table = [starting_team] +\
                [CodenamesTableWidget.ASSASSIN] +\
                [CodenamesTableWidget.BLUE] * 8 +\
                [CodenamesTableWidget.RED] * 8 +\
                [CodenamesTableWidget.PASSER_BY] * 7
        random.shuffle(table)
        self.background_color = starting_team
        for rect, color in zip(self._rectangles, table):
            rect.color = color
