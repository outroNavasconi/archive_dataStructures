from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class Box:
    def __init__(self, size, point: Point):
        self.size = size
        self.point = point
        self.width = size + point.y
        self.height = size + point.x

    def contains(self, point: Point) -> bool:
        return self.x <= point.x <= self.height and self.y <= point.y <= self.width

    def intersectWith(self, box: Box) -> bool:
        pass

class Quadtree:
    def __init__(self, box: Box):
        self.capacity = 4
        self.box = box
        self.elements = []
        self.northWest = None
        self.northEast = None
        self.southWest = None
        self.southEast = None

    def insert(self, point: Point):
        if not self.box.contains(point):
            return False
        
        if len(self.elements) < self.capacity and self.northWest == None:
            self.elements.append(point)
            return True
        
        if self.northWest == None:
            self.subdivide()

        if self.northWest.insert(point):
            return True
        
        if self.northEast.insert(point):
            return True

        if self.southWest.insert(point):
            return True
        
        if self.southEast.insert(point):
            return True

        return False

    def subdivide(self):
        half_size = self.box.size / 2
        self.northWest = Box(half_size, Point(self.box.x, self.box.y))
        self.northEast = Box(half_size, Point(self.box.x + half_size, self.box.y))
        self.southWest = Box(half_size, Point(self.box.x, self.box.y + half_size))
        self.southEast = Box(half_size, Point(self.box.x + half_size, self.box.y + half_size))

    def query(self, box: Box):
        pass

