from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
Sky()
player = FirstPersonController()
boxes = []
for n in range(8):
    for k in range(8):
        box = Button(
            parent=scene,
            model='cube',
            origin=0.5,
            textute='white',
            color=color.orange,
            highligt=color.lime,
            position=(k, 0, n)
        )
        boxes.append(box)

    def input(key):
        for box in boxes:
            if box.hovered:
                if key == 'left mouse down':
                    newBox = Button(
                        parent=scene,
                        model='cube',
                        origin=0.5,
                        textute='white',
                        color=color.orange,
                        highligt=color.lime,
                        position= box.position + mouse.normal
                    )
                    boxes.append(newBox)
                if key == 'left mouse down':
                    boxes.remove(box)
                    destroy(box)

app.run()
