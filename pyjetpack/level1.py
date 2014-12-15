# -*- encoding: utf-8 -*-
import cocos
from cocos.scene import Scene
from cocos.text import Label
from cocos.layer import ColorLayer, MultiplexLayer
from cocos.sprite import Sprite
from cocos.actions import FadeIn, MoveBy
from cocos.director import director
import pyglet
from pyglet.window import key


class Character(cocos.sprite.Sprite):

    def __init__(self):
        super(Character, self).__init__('trees.png', position=(220, 240))


#This is the emitter
class Playground(pyglet.event.EventDispatcher):
    is_event_handler = True

    def __init__(self):
        super(Playground, self).__init__()

        x,y = director.get_window_size()
        self.transform_anchor_x = x // 2
        self.transform_anchor_y = y // 2


    def __register_event_type(self):
        self.register_event_type('on_enter')
        self.register_event_type('on_mouse_motion')

def get_newgame():
    layer = (Character())
    return Scene(layer)
