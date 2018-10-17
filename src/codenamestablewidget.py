import random

from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from rectanglewidget import RectangleWidget
from styles import Styles

Builder.load_file("CodenamesTableWidget.kv")


class CodenamesTableWidget(GridLayout):
    """
    Table widget implementation.

    See `CodenamesTableWidget.kv`.
    """

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
        starting_team = Styles.TEAM_RED if random.random() < 0.5 else Styles.TEAM_BLUE
        table = [starting_team] +\
                [Styles.ASSASSIN] +\
                [Styles.TEAM_BLUE] * 8 +\
                [Styles.TEAM_RED] * 8 +\
                [Styles.PASSER_BY] * 7
        random.shuffle(table)
        self.background_color = starting_team
        for rect, color in zip(self._rectangles, table):
            rect.color = color
