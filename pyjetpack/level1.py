# -*- encoding: utf-8 -*-
import cocos
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.tiles import *
from cocos.director import director
import pyglet
from pyglet.window import key

keyboard = key.KeyStateHandler()


class Character(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(Character, self).__init__()
        img = pyglet.image.load('data/kid.png')
        self.sprite = cocos.sprite.Sprite(img)
        self.sprite.scale = 6
        self.sprite.position = 120, 60
        self.add(self.sprite)

        sprite = Sprite('data/trees.png')
        sprite.position = 220, 220
        sprite.opacity = 80
        self.add(sprite, z=0)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.sprite.y += 60
        elif symbol == key.DOWN:
            self.sprite.y -= 60


#This is the emitter
class Playground(pyglet.event.EventDispatcher):
    is_event_handler = True

    def __init__(self):
        super(Playground, self).__init__()

        x,y = director.get_window_size()
        self.transform_anchor_x = x // 2
        self.transform_anchor_y = y // 2


    def __register_event_type(self):
        self.register_event_type('on_key_press')
        self.register_event_type('on_mouse_motion')


def get_newgame():
    global tiles
    player = Character()
    # Try to introduce a tiled map in background WIP.
    scroller = player
    map_layer = tiles.load('level1.xml')['level1']
    scroller.add(player)
    scroller.add(map_layer)


    return Scene(player)
