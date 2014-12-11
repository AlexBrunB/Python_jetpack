# -*- encoding: utf-8 -*-

from cocos.scene import Scene
from cocos.text import Label
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from cocos.actions import FadeIn, MoveBy
from cocos.director import director
import pyglet


class BackgroundLayer(ColorLayer):

    is_event_handler = True

    def __init__(self):
        super(BackgroundLayer, self).__init__(192, 192, 192, 192)

        label = Label(
            'Level 1',
            font_name='Ubuntu Condensed',
            font_size=70,
            anchor_x='center',
            anchor_y='center'
        )


        label.position = 120, 320
        label.do(MoveBy((600, 0), 2))
        self.add(label)

        sprite1 = Sprite('trees.png')
        self.add(sprite1)
        sprite1.position = 220, 220
        sprite1.do(FadeIn(3))

        self.add(sprite1, z=0)

        self.posx = 100
        self.posy = 240
        self.text = Label('Mouse Event', font_size=18, x=self.posx, y=self.posy )
        self.add( self.text )


    def update_text (self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_motion (self, x, y, dx, dy):
        self.update_text (x, y)

    def on_mouse_drag (self, x, y, dx, dy, buttons, modifiers):
        self.update_text (x, y)

    def on_mouse_press (self, x, y, buttons, modifiers):
        self.posx, self.posy = director.get_virtual_coordinates (x, y)
        self.update_text (x,y)

#This is the emitter
"""
class Playground(pyglet.event.EventDispatcher):
    is_event_handler = True


    def __init__(self):
        super(Playground, self).__init__()

    def __register_events(self):
        self.register_event_type('on_jump')

"""
#
#  This is the listener
#  Listener provide actions
#  But i'm not able allready to add function move for the Character on the Class BackgroundLayer
#
"""
class Character(object):
    def __init__(self):
        self.sprite = []

        self.posx = 100
        self.posy = 240
        self.add( self.Sprite('car.gif', x=self.posx, y=self.posy ) )
"""



def get_newgame():
    layer = BackgroundLayer()
    return Scene(layer)

