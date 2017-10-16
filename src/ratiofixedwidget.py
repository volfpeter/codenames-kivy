from kivy.uix.widget import Widget
from kivy.properties import AliasProperty
from kivy.properties import NumericProperty


class RatioFixedWidget(Widget):
    """
    Widget that always shows its content with a fixed ratio, maximized in the available space.
    """

    ratio = NumericProperty(1)

    def get_effective_size(self):
        width, height = self.size
        ratio = self.ratio
        new_width = min(width, height * ratio)
        new_height = new_width / ratio
        if new_height > height:
            new_height = height
            new_width = new_height * ratio
        return new_width, new_height

    effective_size = AliasProperty(get_effective_size, None, bind=("size", "ratio"))
