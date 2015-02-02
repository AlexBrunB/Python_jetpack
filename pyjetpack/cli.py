# -*- encoding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

## Je comprends pas pourquoi j'ai un sapin de Noël dans les imports!!
from cocos.scene import Scene
from cocos.menu import Menu
from cocos.layer import ColorLayer
from cocos.menu import MenuItem, MultiplexLayer, ToggleMenuItem
from cocos.menu import MultipleMenuItem
from cocos.menu import fixedPositionMenuLayout
from cocos.scenes.transitions import FlipAngular3DTransition
from cocos.director import director
from pyjetpack import soundex
from pyjetpack.level1 import get_newgame
import pyglet

class BackgroundLayer(ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__(128, 128, 192, 80)


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("Main menu")

        #soundex.set_music('space_oddity.ogg')

        items = [
            MenuItem('Jouer', self.on_new_game),
            MenuItem('Options', self.on_options),
            MenuItem('Scores', self.on_scores),
            MenuItem('Quitter', self.on_quit),
        ]
        items[0].scale = 1.2
        self.create_menu(items,
                         layout_strategy=fixedPositionMenuLayout(
                             [(450, 300), (130, 200), (200, 100), (400, 50)]))


    def on_new_game(self):
        director.push(FlipAngular3DTransition(get_newgame()))

    def on_options(self):
        self.parent.switch_to(1)

    def on_scores(self):
        self.parent.switch_to(2)

    def on_quit(self):
        pyglet.app.exit()


class OptionMenu(Menu):
    def __init__(self):
        super(OptionMenu, self).__init__("Options menu")

        l = [
            MenuItem('Back', self.on_quit),
            MenuItem('Fullscreen', self.on_fullscreen),
            MenuItem('Volumes', self.on_volumes),
            ToggleMenuItem('Show FPS: ', self.on_show_fps, True),
        ]

        self.create_menu(l)

    def on_quit(self):
        self.parent.switch_to(0)

    def on_show_fps(self, value):
        director.show_FPS = value

    def on_volumes(self):
        self.parent.switch_to(3)

    def on_fullscreen(self):
        director.window.set_fullscreen(not director.window.fullscreen)


class VolumesMenu(Menu):
    def __init__(self):
        super(VolumesMenu, self).__init__("Volumes menu")
        self.volumes = [
            'Mute',
            '10',
            '20',
            '30',
            '40',
            '50',
            '60',
            '70',
            '80',
            '90',
            '100',
        ]

        items = [
            MenuItem('Back', self.on_quit),
            MultipleMenuItem(
                'SFX volume: ',
                self.on_sfx_volume,
                self.volumes,
                int(soundex.sound_vol * 10)
            ),
            MultipleMenuItem(
                'Music volume: ',
                self.on_music_volume,
                self.volumes,
                int(soundex.music_player.volume * 10)
            ),
        ]

        self.create_menu(items)

    def on_quit(self):
        self.parent.switch_to(1)

    def on_sfx_volume(self, idx):
        vol = idx / 10.0
        soundex.sound_volume(vol)

    def on_music_volume(self, idx):
        vol = idx / 10.0
        soundex.music_volume(vol)


class ScoreMenu(Menu):
    def __init__(self):
        super(ScoreMenu, self).__init__("Score menu")

        self.font_title['font_name'] = 'You Are Loved'
        self.font_title['font_size'] = 48
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'You Are Loved'

        self.create_menu([MenuItem('Go Back', self.on_quit)])

    def on_quit(self):
        self.parent.switch_to(0)


def main():

    pyglet.resource.path.append('@pyjetpack.data')
    pyglet.resource.reindex()
    window = director.init(resizable=True)
    director.window = window
    scene = Scene(
        BackgroundLayer(),
        MultiplexLayer(MainMenu(), OptionMenu(), ScoreMenu(), VolumesMenu())
    )
    director.run(scene)

if __name__ == "__main__":
    main()
