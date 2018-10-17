"""
Style declarations.
"""

from kivy.utils import rgba


class ElementaryColors(object):
    """
    A selection of colors from Elementary OS's style guide.
    """

    BLACK_700 = rgba("#1a1a1a")

    BLUEBERRY_700 = rgba("#0d52bf")

    LIME_700 = rgba("#3a9104")

    ORANGE_700 = rgba("#cc3b02")

    SLATE_100 = rgba("#95a3ab")
    SLATE_700 = rgba("#273445")
    SLATE_900 = rgba("#0e141f")


class Styles(object):
    """
    Style declarations for the application.
    """

    BACKGROUND = ElementaryColors.SLATE_900
    BORDER = ElementaryColors.BLACK_700
    TEXT = ElementaryColors.SLATE_100

    ASSASSIN = ElementaryColors.SLATE_700
    PASSER_BY = ElementaryColors.LIME_700
    TEAM_RED = ElementaryColors.ORANGE_700
    TEAM_BLUE = ElementaryColors.BLUEBERRY_700
