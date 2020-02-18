from PIL import Image, ImageDraw
from reply import World, generate_routes

colors = {
    '#': (87, 62, 0,  255),
    '~': (68, 171,219,255),
    '*': (0,  0,  0,  255),
    '+': (179,157,73, 255),
    'X': (0,  0,  0,  255),
    '_': (0,  0,  0,  255),
    'H': (0,  0,  0,  255),
    'T': (0,  0,  0,  255),
}

if __name__ == '__main__':
    world = World()
    image = Image.new("RGBA", (world.width*8,world.height*8))
    draw = ImageDraw.Draw(image)

    for y in range(world.height):
        for x in range(world.width):
            v = world.get(x, y)
            color = colors.get(v, (255,255,255,255))
            draw.rectangle([x*10, y*10, x*10+10, y*10+10], fill=color)
    image.show()
    input()
    result = generate_routes(world)

