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
            (MenuItem('Options', self.on_quit ) ),
            (MenuItem('Quitter', self.on_quit )),
        ]

        self.create_menu( items, shake(), shake_back() )

    def on_play(self ):
        pyglet.app.run()

    def on_quit(self ) :
        pyglet.app.exit()

class Background(cocos.layer.ColorLayer):
    def __init__(self):
        super( Background, self ).__init__( 192,192,192,80)


def main():
    pyglet.font.add_directory('.')
    cocos.director.director.init()

    layer = Background ()

    cocos.director.director.run ( Scene( MainMenu(), Background() ) )

if __name__ == "__main__":
    main()

