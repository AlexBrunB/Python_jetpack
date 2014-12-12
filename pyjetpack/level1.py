# -*- encoding: utf-8 -*-
import cocos
from cocos.scene import Scene
from cocos.text import Label
from cocos.layer import ColorLayer, MultiplexLayer
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
        self.add(self.text)

    def update_text(self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_motion(self, x, y, dx, dy):
        self.update_text(x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.update_text(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.posx, self.posy = director.get_virtual_coordinates(x, y)
        self.update_text(x, y)


#This is the emitter
class Playground(cocos.layer.ScrollableLayer, pyglet.event.EventDispatcher):
    is_event_handler = True

    def __init__(self):
        super(Playground, self).__init__()

        x,y = director.get_window_size()
        self.transform_anchor_x = x // 2
        self.transform_anchor_y = y // 2

    def __register_event_type(self):
        self.register_event_type('on_enter')
        self.register_event_type('on_activate')

    def on_enter(self):
        director.push_handlers(self.on_cocos_resize)
        super(Character, self).on_enter()
        self.parent.switch_to(1)


#And this is the listener
# First at all, i can't find the action to add sprite as an object or to create an object
## And I don't figure why this class is not in BackgroundLayer
class Character(object):
    def __init__(self):

        sprite = Sprite('car.gif')
        sprite.position = 220, 220
        sprite.do(FadeIn(3))
        #self.add(sprite, z=0)

    def on_activate(self):
        playground = Playground()
        playground.switch_to(1)


def get_newgame():
    scroller = cocos.layer.ScrollingManager(viewport=director.window)
    scroller.add(Playground(), Character())
    layer = BackgroundLayer()
    return Scene(layer)
