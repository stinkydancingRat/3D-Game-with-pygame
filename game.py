import pygame
import math
from triangle import Triangle

pygame.init()

w, h = 800, 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("3D Game")

clock = pygame.time.Clock()

running = True

circles = []

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]


camera_x = 0
camera_y = -200
camera_z = 0
camera_yaw = 0
camera_pitch = 0
camera_roll = 0
camera_fov = 90
viewer_distance = 300
camera_speed = 15


triangles = []

def spawn_triangle(p1, p2, p3, color, triangles):
    triangles.append(((p1, p2, p3), color))

spawn_triangle(
    (0, 0, 0),
    (100, 0, 0),
    (0, 0, 100),
    (255, 255, 255), triangles)

def project_point(x, y, z, screen_w, screen_h, fov, viewer_distance):
    # Prevent division by zero by ensuring y is never equal to -viewer_distance
    if y <= -viewer_distance + 1:
        y = -viewer_distance + 1
        
    scale = fov / (viewer_distance + y)
    screen_x = x * scale + screen_w // 2
    screen_y = z * scale + screen_h // 2
    return (int(screen_x), int(screen_y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    forward_speed = camera_speed / (1 + abs(camera_y) / 100)

    if keys[pygame.K_w]:
        camera_y += forward_speed * math.cos(camera_yaw)
        camera_x -= forward_speed * math.sin(camera_yaw)
        camera_z += forward_speed * math.sin(camera_pitch)
    if keys[pygame.K_s]:
        camera_y -= forward_speed * math.cos(camera_yaw)
        camera_x += forward_speed * math.sin(camera_yaw)
        camera_z -= forward_speed * math.sin(camera_pitch)

    if keys[pygame.K_a]:
        camera_x -= camera_speed * math.cos(camera_yaw)
        camera_y += camera_speed * math.sin(camera_yaw)
    if keys[pygame.K_d]:
        camera_x += camera_speed * math.cos(camera_yaw)
        camera_y -= camera_speed * math.sin(camera_yaw)

    if keys[pygame.K_q]:
        camera_z -= camera_speed
    if keys[pygame.K_e]:
        camera_z += camera_speed

    # Sort by depth
    triangles.sort(key=lambda triangle: triangle[0][1], reverse=True)
    
    # Rendering


    screen.fill((0, 0, 0))


    # Draw the triangles
    for triangle in triangles:
        p1, p2, p3 = triangle[0]
        color = triangle[1]

        rel_y1 = p1[1] - camera_y
        rel_y2 = p2[1] - camera_y
        rel_y3 = p3[1] - camera_y

        # Skip rendering if behind camera
        if rel_y1 <= -viewer_distance and rel_y2 <= -viewer_distance and rel_y3 <= -viewer_distance:
            continue

        projected_p1 = project_point(p1[0] - camera_x, rel_y1, p1[2] - camera_z, w, h, camera_fov, viewer_distance)
        projected_p2 = project_point(p2[0] - camera_x, rel_y2, p2[2] - camera_z, w, h, camera_fov, viewer_distance)
        projected_p3 = project_point(p3[0] - camera_x, rel_y3, p3[2] - camera_z, w, h, camera_fov, viewer_distance)

        pygame.draw.polygon(screen, color, [projected_p1, projected_p2, projected_p3])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()