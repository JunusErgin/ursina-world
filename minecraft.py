from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

boxes = []

def random_color():
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    return color.rgb(red, green, blue)

def add_box(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color=random_color(),
        position=position,
        texture='grass'
      )
    )

for x in range(20):
  for y in range(20):
    add_box( (x, 0, y) )

def input(key):
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                add_box(box.position + mouse.normal)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)


app.run()
