
import cocos
from cocos.director import director
from cocos.sprite import Sprite


class BackgroundLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__( 192,192,192,80)

        x,y = director.get_window_size()

        label = cocos.text.Label('Python JetPack',
            font_name='Ubuntu Condensed',
            font_size=32,
            anchor_x='center', anchor_y='center')

        label.position = 120, 320
        self.add(label)

        sprite = cocos.sprite.Sprite('trees.png')
        sprite.position = 220,220
        sprite.opacity = 150
        sprite.scale = 1



        self.add(sprite, z=0)

def get_newgame():

    layer = BackgroundLayer()

    return cocos.scene.Scene (layer)



