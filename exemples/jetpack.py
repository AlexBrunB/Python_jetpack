from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

testinfo = "s, q"
tags = "menu, menu_valign, menu_halign"

from pyglet import image
from pyglet.gl import *
from pyglet import font

from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *

class MainMenu(Menu):
    def __init__(self):
        super( MainMenu, self).__init__("JetPack Python")

        self.menu_valign = CENTER
        self.menu_halign = CENTER

        items = [
            (MenuItem('Options', self.on_quit ) ),
            (MenuItem('Quit', self.on_quit )),
        ]

        self.create_menu( items, shake(), shake_back() )


    def on_quit(self ) :
        pyglet.app.exit()


def main():
    pyglet.font.add_directory('.')

    director.init( resizable=True)
    director.run ( Scene( MainMenu() ) ) 

if __name__=='__main__':
    main()

