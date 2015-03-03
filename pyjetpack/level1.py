# -*- encoding: utf-8 -*-
import cocos
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.actions import MoveTo, MoveBy, FadeIn
import pyglet
from pyglet.window import key


keyboard = key.KeyStateHandler()

class Character(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Character, self).__init__(192, 192, 192, 80)
        img = pyglet.image.load('data/trees.png')
        self.sprite = cocos.sprite.Sprite(img)
        self.sprite.position = 220, 220
        self.sprite.opacity = 60
        self.add(self.sprite, z=0)

        img = pyglet.image.load('data/kid.png')
        self.sprite = cocos.sprite.Sprite(img)
        self.sprite.scale = 6
        self.sprite.velocity = (120, 120)
        self.sprite.position = 120, 60
        self.add(self.sprite)

        self.label = cocos.text.Label('Level 1',
            font_name='Tlwg Typist',
            font_size=42,
            x=320, y=400,
            anchor_x='center',
            anchor_y='center')
        self.label.do(MoveBy((0, 120), 4))
        self.label.set_focus = (15, 15)
        self.label.force_focus = (15, 15)
        self.add(self.label)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.sprite.x += 80
        elif symbol == key.LEFT:
            self.sprite.x -= 80
        elif symbol == key.UP:
            self.sprite.y += 80
        elif symbol == key.DOWN:
            self.sprite.y -= 80


class Enemy(cocos.layer.ColorLayer):

    def __init__(self):
        super(Enemy, self).__init__(192, 192, 192, 80)
        img = pyglet.image.load('data/poulpi.png')
        self.sprite = cocos.sprite.Sprite(img)
        self.sprite.position = 120, 350
        self.sprite.opacity = 60



class PauseScene(Scene):
    '''Pause Scene'''
    def __init__(self, background, *layers):
        super(PauseScene, self).__init__(*layers)
        self.bg = background
        self.width, self.height = self.director.get_window_size()
        self.director.pause();


class ScrollableLayer(cocos.layer.Layer):
    ''' Introduce Scrollable Layer
        Also need the ScrollingManager'''
    view_x, view_y = 100, 100
    view_w, view_h = 100, 100
    origin_x = origin_y = origin_z = 0
    img = pyglet.image.load('data/kid.png')

    def __init__(self, parallax=1):
        super(ScrollableLayer, self).__init__()
        self.parallax = parallax

        self.transform_anchor_x = 0
        self.transform_anchor_y = 0

        self.batch = pyglet.graphics.Batch()

    def on_enter(self):
        self.director.push_handlers(self.on_cocos_resize)
        super(ScrollableLayer, self).on_enter()

    def on_exit(self):
        super(ScrollableLayer, self).on_exit()
        self.director.pop_handlers()


class ScrollingManager(cocos.layer.Layer):
    """Manager will limit scrolling.
    If a layer has no dimensions it will scroll freely and without bound.
    The manager is initialised with the viewport (usually a Window) which has
    the pixel dimensions .width and .height which are used during focusing.
    """
    def __init__(self):
        super(ScrollingManager, self, viewport=None, do_not_scale=None).__init__()
        img = pyglet.image.load('data/trees.png')
        super.self.add(img)

        # map size (cells)
        self.view_x, self.view_y = 128, 128
        self.view_w, self.view_h = 128, 128
        self.childs_ox = 100
        self.childs_oy = 100

        # Focal point on the Layer
        self.fx = self.fy = 0

       # window size (pixels) Don't know what size the screen size?
        self.transform_anchor_x = 960
        self.transform_anchor_y = 640
        # Doesn't work yet
        self.add(ScrollingManager)
        self.update_view_size(ScrollingManager)

    def on_enter(self):
        super(ScrollingManager, self).on_enter()
        self.director.push_handlers(self.on_cocos_resize)
        self.update_view_size()
        self.refresh_focus()



def get_newgame():

    player = Character()
    main_scene = cocos.scene.Scene(player)
    return Scene(player)
