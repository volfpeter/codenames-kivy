import os
import random

from kivy.app import App
from kivy.config import Config
from kivy.properties import StringProperty

# This import may not be used, but it is necessary for Kivy.
from codenamestablewidget import CodenamesTableWidget

Config.set("graphics", "width", "680")
Config.set("graphics", "height", "400")


class CodenamesApp(App):

    WORDLIST_NAMES = ("English", "Hungarian")

    word = StringProperty("")
    wordlist_name = StringProperty(WORDLIST_NAMES[0])

    def __init__(self, *args, **kwargs):
        """
        Initialization.
        """
        super(CodenamesApp, self).__init__(*args, **kwargs)

        self.word_list = ()
        """The word list to choose from."""

        # Initialize the word list.
        self.on_wordlist_name(None, self.wordlist_name)

    def on_wordlist_name(self, instance, value):
        """
        Handler called when the value of the `wordlist_name` property has changed.
        """
        if value == "English":
            from wordlists.words_en import get_words
            self.word_list = get_words()
        elif value == "Hungarian":
            from wordlists.words_hu import get_words
            self.word_list = get_words()

    def new_random_word(self):
        """
        Sets the `word` property to a new randomly selected word from the word list.
        """
        if len(self.word_list) == 0:
            self.word = "Empty word list."
        else:
            self.word = random.choice(self.word_list)


if __name__ == "__main__":
    CodenamesApp().run()
