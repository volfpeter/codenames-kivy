Codenames - Kivy
=====================

Table and word list generator for the popular Codenames_ boardgame, created
in Python 3 using Kivy_.

Dependencies
=================

The only dependency of the project is Kivy, see Kivy's installation_ instructions.

Word lists
===============

The application needs a word list to be able to suggest words randomly to you
so you can set up a board. Some word lists are included in this project, see
the wordlists_ directory.

The application will read words from the ``wordlist.wl`` file that is next to
the source files. This word list file is empty by default, it's up to you to
fill it with words by either copying the content of one of the included word
list files to ``wordlist.wl`` or by acquiring a word list from some other source.

How to run
===============

If you have Python 3 and Kivy_ installed, then you will be able to run the application
from terminal or command line by executing ``main.py``.

You should also be able to create an Android or iOS application from this codebase
by following the corresponding instructions on the Kivy packaging_ website.

Legal notice
=================

This code has been open sourced after written permission from the publisher_
Czech Games Edition. Please keep this - and the attached license - in mind
when using this project.

License - GNU AGPLv3
=========================

This code has been open sourced after written permission from the publisher_,
as a result the project uses the GNU AGPLv3 license.


.. _Codenames: https://czechgames.com/en/codenames/
.. _installation: https://kivy.org/#download
.. _Kivy: https://kivy.org/#home
.. _packaging: https://kivy.org/docs/guide/packaging.html
.. _publisher: https://czechgames.com/en/
.. _wordlists: https://github.com/volfpeter/codenames-kivy/tree/master/wordlists
