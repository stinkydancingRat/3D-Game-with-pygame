import pygame
import math
from triangle import Triangle
from rectangle import Rectangle

pygame.init()

w, h = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
pygame.display.set_caption("3D Game")

clock = pygame.time.Clock()
running = True

colors = [
    (255, 0, 0),   
    (0, 255, 0),   
    (0, 0, 255),   
    (255, 255, 0), 
    (0, 255, 255), 
    (255, 0, 255), 
    (128, 0, 0),   
    (0, 128, 0),   
    (0, 0, 128),   
    (128, 128, 0), 
    (0, 128, 128), 
    (128, 0, 128)  
]

camera_x = 0
camera_y = -200
camera_z = 0
camera_yaw = 0
camera_pitch = 0
camera_roll = 0
camera_fov = 90
viewer_distance = 300
camera_speed = 15

cubes = []
cube = Rectangle(0, 0, 0, 100, 10, 100, colors)
cube.create_rectangle()
cubes.append(cube)

def project_point(x, y, z, screen_w, screen_h, fov, viewer_distance):
    if y <= -viewer_distance + 1:
        y = -viewer_distance + 1
    scale = fov / (viewer_distance + y)
    screen_x = x * scale + screen_w // 2
    screen_y = z * scale + screen_h // 2
    return (int(screen_x), int(screen_y))

pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:   
        running = False

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
        camera_z += camera_speed
    if keys[pygame.K_e]:
        camera_z -= camera_speed



    screen.fill((0, 0, 0))

    for cube in cubes:
        for triangle in cube.triangles:
            triangle.draw(screen, camera_x, camera_y, camera_z, w, h, camera_fov, viewer_distance, project_point)


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
