from triangle import Triangle

class Rectangle:
    def __init__(self, x, y, z, width, height, depth, color):
        self.x, self.y, self.z = x, y, z
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color
        self.currentcolorindex = 0
        self.triangles = []
        
    def create_rectangle(self):
        # 8 corner points of the box
        p = [
            (self.x, self.y, self.z),
            (self.x + self.width, self.y, self.z),
            (self.x + self.width, self.y + self.height, self.z),
            (self.x, self.y + self.height, self.z),
            (self.x, self.y, self.z + self.depth),
            (self.x + self.width, self.y, self.z + self.depth),
            (self.x + self.width, self.y + self.height, self.z + self.depth),
            (self.x, self.y + self.height, self.z + self.depth)
        ]

        faces = [
            (0, 1, 2, 3),  # Front
            (4, 5, 6, 7),  # Back
            (0, 1, 5, 4),  # Bottom
            (2, 3, 7, 6),  # Top
            (1, 2, 6, 5),  # Right
            (0, 3, 7, 4)   # Left
        ]

        for i, (a, b, c, d) in enumerate(faces):
            color = self.color[i % len(self.color)] 
            self.triangles.append(Triangle(p[a], p[b], p[c], color))
            self.triangles.append(Triangle(p[a], p[c], p[d], color))
            self.currentcolorindex += 1
