import io, sys

class HQ:
    def __init__(self, x, y, reward):
        self.x = x
        self.y = y
        self.reward = reward

class World:
    def __init__(self):
        cc = [ int(v) for v in input().split() ]
        [ self.width, self.height, hq_amount, self.max_offices ] = cc
        self.hqs = [ ]
        for hq_index in range(hq_amount):
            [ x, y, reward ] = [ int(v) for v in input().split() ]
            self.hqs.append(HQ(x, y, reward))
        self.cells = [ ]
        for row_index in range(self.height):
            self.cells.extend(input().strip())


    def get(self, x, y):
        idx = y * self.width + x
        if idx < len(self.cells):
            return self.cells[idx]
        else:
            return '#'

def generate_routes(world):
    result = [ ]

    sorted_hqs = sorted(world.hqs, key=lambda t: t.reward, reverse=True)
    for office_index in range(world.max_offices):
        hq = sorted_hqs[office_index]
        if world.get(hq.x, hq.y + 1) != '#':
            result.append([hq.x, hq.y + 1, 'U'])
        elif world.get(hq.x, hq.y - 1) != '#':
            result.append([hq.x, hq.y - 1, 'D'])
        elif world.get(hq.x + 1, hq.y) != '#':
            result.append([hq.x + 1, hq.y, 'L'])
        elif world.get(hq.x - 1, hq.y) != '#':
            result.append([hq.x - 1, hq.y, 'R'])

    return result

if __name__ == '__main__':
    world = World()
    result = generate_routes(world)

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, newline='\n')
    for r in result:
        print(f'{r[0]} {r[1]} {r[2]}', end='\n')
