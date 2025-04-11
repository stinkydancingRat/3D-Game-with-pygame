import pygame

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = (255, 255, 255)
    

    def sort_vertices(self):
        self.p1, self.p2, self.p3 = sorted([self.p1, self.p2, self.p3], key=lambda p: p[1])
    
    

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [self.p1, self.p2, self.p3])