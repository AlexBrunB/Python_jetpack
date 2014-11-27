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
        super( MainMenu, self).__init__("JetPack Python")

        self.menu_valign = CENTER
        self.menu_halign = CENTER

        items = [
            (MenuItem('Jouer', self.on_play ) ),
            (MenuItem('Options', self.on_options ) ),
            (MenuItem('Quitter', self.on_quit )),
        ]

        self.create_menu( items, shake(), shake_back() )

    def on_play(self ):
        pyglet.app.run()

    def on_options(self):
        self.parent.switch_to(1)

    def on_quit(self ) :
        pyglet.app.exit()

class OptionsMenu(cocos.layer.Layer):
    def __init__(self):
        super(MainMenu, self).__init__()


def main():
    pyglet.font.add_directory('.')

    director.init( resizable=True)

    layer = cocos.layer.ColorLayer(192,192,192,80)

    main_scene = cocos.scene.Scene (layer)

    director.run ( Scene(MultiplexLayer( MainMenu(),main_scene) ))


if __name__ == "__main__":
    main()

