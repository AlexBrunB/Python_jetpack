
import cocos
from cocos.actions import *


class Character(cocos.layer.ColorLayer):
    def __init__(self):
        super( Character, self ).__init__( 192,192,192,192)

        label = cocos.text.Label('Level 1!',
            font_name='Ubuntu Condensed',
            font_size=64,
            anchor_x='center', anchor_y='center')

        label.position = 220,40
        self.add( label )


        sprite = cocos.sprite.Sprite('sam.png')
        sprite.position = 120, 320

        sprite.scale = 1

        self.add( sprite, z=0 )


if __name__ == "__main__":
    cocos.director.director.init()


    layer = Character ()

    layer.do( RotateBy(360, duration=1))

    main_scene = cocos.scene.Scene (layer)

    cocos.director.director.run (main_scene)


