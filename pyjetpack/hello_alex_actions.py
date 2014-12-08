
import cocos
from cocos.actions import *


class HelloAlex(cocos.layer.ColorLayer):
    def __init__(self):
        # background color
        super( HelloAlex, self ).__init__( 64,64,224,255)

		# label is a wrapper that contain your string
        label = cocos.text.Label('Hello, Alex!',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')

        # set the label in the center of the screen
        label.position = 320,240
        self.add( label )
        
        
        sprite = cocos.sprite.Sprite('blackswan.png')
        sprite.position = 320,240
        
        # sprite scale attribute starts with 0.5 (default 1 )
        sprite.scale = 0.5
        
        # add the sprite as a child, but with z=1 (default is z=0).
        # this means that the sprite will be drawn on top of the label
        self.add( sprite, z=1 )

        # create a ScaleBy action that lasts 2 seconds
        scale = ScaleBy(3, duration=2)
        
        # tell the label to scale and scale back and repeat these 2 actions forever
        label.do( Repeat( scale + Reverse( scale) ) )
        
        # tell the sprite to scaleback and then scale, and repeat these 2 actions forever
        sprite.do( Repeat( Reverse(scale) + scale ) )

if __name__ == "__main__":
    cocos.director.director.init()

    
    hello_layer = HelloAlex ()
    
    # tell the layer to perform a Rotate action in 10 seconds.
    hello_layer.do( RotateBy(360, duration=10) )

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene (hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run (main_scene)

   
