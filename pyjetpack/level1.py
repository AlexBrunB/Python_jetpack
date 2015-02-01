# -*- encoding: utf-8 -*-
import cocos
from cocos.scene import Scene
from cocos.actions import MoveBy, FadeIn
from cocos.sprite import Sprite
import pyglet
from pyglet.window import key

keyboard = key.KeyStateHandler()


class Character(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(Character, self).__init__()
        sprite = Sprite('data/trees.png')
        sprite.position = 220, 220
        sprite.opacity = 60
        self.add(sprite, z=0)

        img = pyglet.image.load('data/kid.png')
        self.sprite = cocos.sprite.Sprite(img)
        self.sprite.scale = 6
        self.sprite.position = 120, 60
        self.sprite.do(FadeIn(8))
        self.add(self.sprite)

        self.label = cocos.text.Label('Level 1',
            font_name='Tlwg Typist',
            font_size=42,
            x=320, y=400,
            anchor_x='center',
            anchor_y='center')
        self.label.do(MoveBy((0, 120), 4))
        self.add(self.label)



    def on_key_press(self, symbol):
        if symbol == key.UP:
            self.sprite.y += 60
        elif symbol == key.DOWN:
            self.sprite.y -= 60


def get_newgame():

    player = Character()
    main_scene = cocos.scene.Scene(player)
    return Scene(main_scene)
