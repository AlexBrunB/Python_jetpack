# -*- encoding: utf-8 -*-
import cocos
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.director import director
import pyglet
from pyglet.window import key

keyboard = key.KeyStateHandler()


class Character(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(Character, self).__init__()
        img = pyglet.image.load('car.gif')
        self.sprite = cocos.sprite.Sprite(img)
        self.sprite.scale = 3
        self.sprite.position = 220, 60
        self.add(self.sprite)

        sprite = Sprite('trees.png')
        sprite.position = 220, 220
        sprite.opacity = 80
        self.add(sprite, z=0)

    def on_key_press(self, symbol, modifiers):
        print 'pressing'
        if symbol == key.RIGHT:
            self.sprite.x += 60
        elif symbol == key.LEFT:
            self.sprite.x -= 60
        elif symbol == key.SPACE:
            self.sprite.y += 30


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
    player = Character()
    return Scene(player)
