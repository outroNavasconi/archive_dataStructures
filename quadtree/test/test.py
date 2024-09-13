import pygame
from random import randint
from quadtree import Point, Quadtree, Box

DRAW = True

CAPACITY = 4
WIDTH = HEIGHT = 400
POINTS_TO_CREATE = 256

points = []
pointsCount = 0
quadtree = Quadtree(Box(Point(0, 0), WIDTH, HEIGHT), CAPACITY)

for i in range(POINTS_TO_CREATE):
    p = Point(randint(10, WIDTH-10), randint(10, HEIGHT-10))
    quadtree.insert(p)
    points.append(p)

for quad in quadtree.getQuads(quadtree):
    pointsCount += len(quad.points)
    assert len(quad.points) <= CAPACITY, f'the quadtree\'s point capacity has exceeded the maximum allowed ({CAPACITY})'

assert pointsCount == POINTS_TO_CREATE, f'the number of points counted is not the same as expected, count: {pointsCount} expected: {POINTS_TO_CREATE}'

if DRAW:
    running = True

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    screen.fill('black')
    
    for box in quadtree.getBoxes(quadtree):
        rect = pygame.Rect(box.origin.x, box.origin.y, box.width, box.height)
        pygame.draw.rect(screen, 'blue', rect, 1)

    for point in points:
        pygame.draw.circle(screen, 'white', (point.x, point.y), 2)

    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

