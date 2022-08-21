from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(borderless=False)

window.cog_button.enabled = False
mouse.locked = False

mine = Audio('assets/Mine', autoplay=False)
place = Audio('assets/Place', autoplay=False)
punch = Audio('assets/punch', autoplay=False)
music = Audio('assets/music', autoplay=True)

blocks = [
    load_texture('assets/slime.png'), # 0
    load_texture('assets/grass.png'),
    load_texture('assets/dirt.png'),
    load_texture('assets/stone.png'),
    load_texture('assets/wood.png'),
    load_texture('assets/glass.png'),
    load_texture('assets/slime.png'),
    load_texture('assets/slime.png'),
    load_texture('assets/slime.png'),
    load_texture('assets/slime.png'), # 9
    load_texture('assets/bedrock.png'), # over limit
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
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

    if player.position.y < -8:
        player.position = Vec3(0,1,0)

#hotbar
hotbar1 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/grass.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(-0.45, -0.4375)
)

hotbar2 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/dirt.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(-0.35, -0.4375)
)

hotbar3 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/stone.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(-0.25, -0.4375)
)

hotbar4 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/wood.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(-0.15, -0.4375)
)

hotbar5 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/glass.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(-0.05, -0.4375)
)

hotbar6 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/slime.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(0.05, -0.4375)
)

hotbar7 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/wip.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(0.15, -0.4375)
)

hotbar8 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/wip.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(0.25, -0.4375)
)

hotbar9 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/wip.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(0.35, -0.4375)
)

hotbar10 = Entity(
    parent=camera.ui,
    model='assets/block',
    texture='assets/hotbar/wip.png',
    scale=0.05,
    rotation=Vec3(0, 0, 0),
    position=Vec2(0.45, -0.4375)
)

# bedrock layer
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/bedrock.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=1,
            texture=texture,
            color=color.color(0, 0, 1),
            scale=1,
        )



for z in range(-10, 10, 2):
    for x in range(-10, 10, 2):
        voxel = Voxel(position=(x, -6, z))

# stone layer
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/stone.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=1,
            texture=texture,
            color=color.color(0, 0, 1),
            scale=1,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                place.play()
                Voxel(position=self.position + (mouse.normal)*2, texture=blocks[block_id])
            elif key == 'left mouse down':
                mine.play()
                destroy(self)



for z in range(-10, 10, 2):
    for x in range(-10, 10, 2):
        voxel = Voxel(position=(x, -4, z))

        # dirt layer
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/dirt.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=1,
            texture=texture,
            color=color.color(0, 0, 1),
            scale=1,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                place.play()
                Voxel(position=self.position + (mouse.normal)*2, texture=blocks[block_id])
            elif key == 'left mouse down':
                mine.play()
                destroy(self)



for z in range(-10, 10, 2):
    for x in range(-10, 10, 2):
        voxel = Voxel(position=(x, -2, z))

        # grass layer
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=1,
            texture=texture,
            color=color.color(0, 0, 1),
            scale=1,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                place.play()
                Voxel(position=self.position + (mouse.normal)*2, texture=blocks[block_id])
            elif key == 'left mouse down':
                mine.play()
                destroy(self)



for z in range(-10, 10, 2):
    for x in range(-10, 10, 2):
        voxel = Voxel(position=(x, 0, z))


player = FirstPersonController(jump_height = 2, height =2)
app.run()
