from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class Box:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def isInside(self, point):
        x, y = self.origin.x, self.origin.y
        return x <= point.x < x + self.width and y <= point.y < y + self.height

    def intersectWith(self, another):
        pass

class Quadtree:
    def __init__(self, box, capacity = 4):
        self.box = box
        self.capacity = capacity
        self.points = []
        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None

    def insert(self, point):
        if not self.box.isInside(point):
            return False

        if self.northwest:
            self.northwest.insert(point)
            self.northeast.insert(point)
            self.southwest.insert(point)
            self.southeast.insert(point)
            return True
        
        self.points.append(point)
        if len(self.points) > self.capacity:
            return self.subdivide()

    def subdivide(self):
        halfWidth = self.box.width / 2
        halfHeight = self.box.height / 2
        x, y = self.box.origin.x, self.box.origin.y
        self.northwest = Quadtree(Box(Point(x, y), halfWidth, halfHeight))
        self.northeast = Quadtree(Box(Point(x + halfWidth, y), halfWidth, halfHeight))
        self.southwest = Quadtree(Box(Point(x, y + halfHeight), halfWidth, halfHeight))
        self.southeast = Quadtree(Box(Point(x + halfWidth, y + halfHeight), halfWidth, halfHeight))
        for point in self.points:
            self.northwest.insert(point)
            self.northeast.insert(point)
            self.southwest.insert(point)
            self.southeast.insert(point)
        self.points.clear()
        return True

    def query(self):
        pass

    def getBoxes(self, quad):
        if not quad.northwest:
            return [quad.box]
        return [
            *self.getBoxes(quad.northwest),
            *self.getBoxes(quad.northeast),
            *self.getBoxes(quad.southwest),
            *self.getBoxes(quad.southeast)
        ]
    
    def getQuads(self, quad):
        if not quad.northwest:
            return [quad]
        return [
            *self.getQuads(quad.northwest),
            *self.getQuads(quad.northeast),
            *self.getQuads(quad.southwest),
            *self.getQuads(quad.southeast)
        ]
    
