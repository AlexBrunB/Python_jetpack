


import cocos

class HelloAlex(cocos.layer.Layer):
    def __init__(self):
        super( HelloAlex, self ).__init__()


        label = cocos.text.Label('Hello, Alex!',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')

        label.position = 320,240
        self.add( label )

if __name__ == "__main__":

    cocos.director.director.init()


    hello_layer = HelloAlex ()

    
    main_scene = cocos.scene.Scene (hello_layer)

    
    cocos.director.director.run( cocos.scene.Scene( HelloAlex() ) )

