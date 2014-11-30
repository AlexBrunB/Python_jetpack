
import cocos
from cocos.actions import *
from cocos.director import director
from cocos.sprite import Sprite


class Character(cocos.layer.ColorLayer):
    def __init__(self):
        super( Character, self ).__init__( 192,192,192,80)

        x,y = director.get_window_size()

        label = cocos.text.Label('Level 1!',
            font_name='Ubuntu Condensed',
            font_size=64,
            anchor_x='center', anchor_y='center')

        label.position = 120, 320
        self.add( label )


        sprite = cocos.sprite.Sprite('jetpackjoyride_titlecard.jpg')
        sprite.position = 100,220
        sprite.do( MoveBy( (1000,0), duration=2 ) )
        sprite.scale = 1



        self.add( sprite, z=0 )

if __name__ == "__main__":
    cocos.director.director.init()


    layer = Character ()


    main_scene = cocos.scene.Scene (layer)

    cocos.director.director.run (main_scene)


