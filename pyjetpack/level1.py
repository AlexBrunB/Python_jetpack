
import cocos
from cocos.sprite import Sprite
from cocos.actions import FadeIn



class BackgroundLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__( 192,192,192,192)

        sprite = cocos.sprite.Sprite('trees.png')
        sprite.position = 220, 220
        sprite.do(FadeIn(3))


        self.add(sprite, z=0)

def get_newgame():

    layer = BackgroundLayer()

    return cocos.scene.Scene (layer)



