
import cocos
from cocos.sprite import Sprite
from cocos.actions import FadeIn
from cocos import tiles, actions, layer
import pyglet
from pyglet.window import key


class BackgroundLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__( 192,192,192,192)

        label = cocos.text.Label('Level 1',
        font_name='Ubuntu Condensed',
        font_size=64,
        anchor_x='center', anchor_y='center')

        label.position = 120, 320
        self.add(label)

        sprite = cocos.sprite.Sprite('trees.png')
        sprite.position = 220, 220
        sprite.do(FadeIn(3))


        self.add(sprite, z=0)
        

def get_newgame():

    layer = BackgroundLayer()

    return cocos.scene.Scene (layer)



