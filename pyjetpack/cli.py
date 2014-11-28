from __future__ import division, print_function, unicode_literals


from pyglet import image
from pyglet.gl import *
from pyglet import font

from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.actions import *
import cocos
from cocos.actions import *


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("JetPack Python")

        self.menu_valign = CENTER
        self.menu_halign = CENTER

        items = [
            (MenuItem('Jouer', self.on_play)),
            (MenuItem('Options', self.on_options)),
            (MenuItem('Quitter', self.on_quit)),
        ]

        self.create_menu(items, shake(), shake_back())

    def on_play(self):
        self.parent.switch_to(0)

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
