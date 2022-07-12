from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(borderless=False)

window.fps_counter.enabled = True
window.exit_button.visible = False
mouse.locked = False

punch = Audio('assets/punch', autoplay=False)

blocks = [
    load_texture('assets/slime.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/wood.png'),  # 3
    load_texture('assets/glass.png'),  # 4
    load_texture('assets/slime.png'),  # 5
]

block_id = 1

def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]
    elif key == 'escape':
        mouse.locked = not mouse.locked

sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('assets/sky.jpg'),
    scale=500,
    double_sided=True
)

hand = Entity(
    parent=camera.ui,
    model='assets/block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)

def update():
    if held_keys['right mouse'] or held_keys['left mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

    if player.position.y < -5:
        player.position = Vec3(0,1,0)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=1,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=1
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + (mouse.normal)*2, texture=blocks[block_id])
            elif key == 'left mouse down':
                destroy(self)

for z in range(-10, 10, 2):
    for x in range(-10, 10, 2):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController(jump_height = 2)
app.run()
