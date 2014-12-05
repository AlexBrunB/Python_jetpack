from __future__ import division, print_function, unicode_literals


from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.actions import *

from level1 import get_newgame
from cocos.director import director


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("JetPack Python")

        self.menu_valign = CENTER
        self.menu_halign = CENTER

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

        l = []
        l.append( MenuItem('Quit', self.on_quit))
        l.append( MenuItem('Volumes', self.on_quit) )

        self.create_menu(l)


    def on_quit(self):
        self.parent.switch_to(0)


def main():

    director.init(resizable=True)

    scene = Scene(
        MultiplexLayer(MainMenu(), OptionMenu())
        )
    director.run(scene)

if __name__ == "__main__":
    main()
