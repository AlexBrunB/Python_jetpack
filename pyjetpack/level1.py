
import cocos
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions import FadeIn, MoveBy



class BackgroundLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__( 192,192,192,192)

        x,y = director.get_window_size()

        label = cocos.text.Label('Level 1',
            font_name='Ubuntu Condensed',
            font_size=70,
            anchor_x='center', anchor_y='center')

        label.position = 120, 320
        label.do(MoveBy( (600,0), 2 ))
        self.add(label)

        sprite1 = Sprite('trees.png')
        self.add( sprite1 )
        sprite1.position = 220, 200
        sprite1.do(FadeIn(3))

        #sprite2 = Sprite('car.gif')
        #sprite1.add( sprite2 )
        #sprite2.position = -50, -50
        #sprite2.scale = 3


        self.add(sprite1)


def get_newgame():

    layer = BackgroundLayer()

    return cocos.scene.Scene (layer)



