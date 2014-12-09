# -*- encoding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


from cocos.scene import Scene
import pyglet
from cocos.menu import Menu
from cocos.menu import MenuItem, MultiplexLayer
from cocos.menu import shake, shake_back
from cocos.director import director
from pyjetpack import soundex
from pyjetpack.level1 import get_newgame


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("JetPack Python")

        soundex.set_music('space_oddity.mp3')

        items = [
            (MenuItem('Jouer', self.on_new_game)),
            (MenuItem('Options', self.on_options)),
            ( MenuItem('Scores', self.on_scores)),
            (MenuItem('Quitter', self.on_quit)),
        ]
        self.create_menu(items, shake(), shake_back())

    if soundex.set_music('space_oddity.mp3'):
        soundex.play_music('space_oddity.mp3')


    def on_new_game(self):
        director.push(get_newgame())

    def on_options(self):
        self.parent.switch_to(1)

    def on_scores( self ):
        self.parent.switch_to( 2 )

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

class ScoreMenu(Menu):
    def __init__( self ):
        super( ScoreMenu, self ).__init__("JetPack Python" )

        self.font_title['font_name'] = 'You Are Loved'
        self.font_title['font_size'] = 72
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'You Are Loved'

        self.create_menu( [MenuItem('Go Back', self.on_quit)] )

    def on_quit( self ):
        self.parent.switch_to( 0 )


def main():

    pyglet.resource.path.append('@pyjetpack.data')
    pyglet.resource.reindex()
    window = director.init(resizable=True)
    director.window = window
    scene = Scene(MultiplexLayer(MainMenu(), OptionMenu(), ScoreMenu()))
    director.run(scene)

if __name__ == "__main__":
    main()
