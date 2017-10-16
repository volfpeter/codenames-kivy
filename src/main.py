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

    word = StringProperty("")

    def __init__(self, *args, **kwargs):
        super(CodenamesApp, self).__init__(*args, **kwargs)
        self._word_list = None

    @property
    def word_list(self):
        if self._word_list is None:
            self._load_word_list()

        return self._word_list

    def new_random_word(self):
        word_list = self.word_list
        if word_list is None:
            self.word = "Word file not found."

        if len(word_list) == 0:
            self.word = "Empty word list."
        else:
            self.word = random.choice(word_list)

    def _load_word_list(self):
        word_list_file = "wordlist.txt"
        if not os.path.isfile(word_list_file):
            return

        self._word_list = []
        with open(word_list_file, "r") as words:
            for word in words:
                if word:
                    self._word_list.append(word)


if __name__ == "__main__":
    CodenamesApp().run()
