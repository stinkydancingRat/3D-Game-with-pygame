import pygame

class Triangle:
    def __init__(self, p1, p2, p3, color):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color

    def draw(self, screen, camera_x, camera_y, camera_z, w, h, camera_fov, viewer_distance, project_point):
        rel_y1 = self.p1[1] - camera_y
        rel_y2 = self.p2[1] - camera_y
        rel_y3 = self.p3[1] - camera_y

        if rel_y1 <= -viewer_distance and rel_y2 <= -viewer_distance and rel_y3 <= -viewer_distance:
            return

        projected_p1 = project_point(self.p1[0] - camera_x, rel_y1, self.p1[2] - camera_z, w, h, camera_fov, viewer_distance)
        projected_p2 = project_point(self.p2[0] - camera_x, rel_y2, self.p2[2] - camera_z, w, h, camera_fov, viewer_distance)
        projected_p3 = project_point(self.p3[0] - camera_x, rel_y3, self.p3[2] - camera_z, w, h, camera_fov, viewer_distance)

        pygame.draw.polygon(screen, self.color, [projected_p1, projected_p2, projected_p3])