# -*- encoding: utf-8 -*-
from cocos.scene import Scene
from cocos.text import Label
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from cocos.actions import FadeIn, MoveBy


class BackgroundLayer(ColorLayer):
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

        sprite2 = Sprite('car.gif')
        sprite1.add(sprite2)
        sprite2.position = -100, -50
        sprite2.do(MoveBy((300, 0), 1)),
        sprite2.scale = 3

        self.add(sprite1, sprite2)


def get_newgame():
    layer = BackgroundLayer()
    return Scene(layer)



