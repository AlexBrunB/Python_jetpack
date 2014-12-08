# -*- encoding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


from cocos.scene import Scene
import pyglet
from cocos.menu import Menu
from cocos.menu import MenuItem, MultiplexLayer
from cocos.menu import shake, shake_back
from level1 import get_newgame
from cocos.director import director
from pyjetpack import soundex


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("JetPack Python")

        soundex.set_music('space_oddity.mp3')

        items = [
            (MenuItem('Jouer', self.on_new_game)),
            (MenuItem('Options', self.on_options)),
            (MenuItem('Quitter', self.on_quit)),
        ]
        self.create_menu(items, shake(), shake_back())

    def on_new_game(self):
        director.push(get_newgame())

    def on_options(self):
        self.parent.switch_to(1)

    def on_quit(self):
        pyglet.app.exit()


class OptionMenu(Menu):
    def __init__(self):
        super(OptionMenu, self).__init__("JetPack Python")

        l = [
            MenuItem('Quit', self.on_quit),
            MenuItem('Volumes', self.on_quit),
        ]

        self.create_menu(l)

    def on_quit(self):
        self.parent.switch_to(0)


def main():

    pyglet.resource.path.append('@pyjetpack.data')
    pyglet.resource.reindex()
    window = director.init(resizable=True)
    director.window = window
    scene = Scene(MultiplexLayer(MainMenu(), OptionMenu()))
    director.run(scene)

if __name__ == "__main__":
    main()
