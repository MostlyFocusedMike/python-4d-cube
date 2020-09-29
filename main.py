import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

#     y
#     |
#     |
#     |
#     |
#       ------------ X
#    /
#   /
#  /
# z

    # (x, y, z)
verticies2 = [
    [1, -1, -1], # back bottom right
    [1, 1, -1],  # back top right
    [-1, 1, -1], # back top left
    [-1, -1, -1], # back bottom left
    [1, -1, 1],   # front bottom right
    [1, 1, 1],    # front top right
    [-1, -1, 1],  # front bottom left
    [-1, 1, 1]    # front top left
]

def Cube2(transform):
    verticies2[0][0] = transform * .1 + 1
    verticies2[0][2] = transform * .1 + 1
    verticies2[1][0] = transform * .1 + 1
    verticies2[2][0] = transform * -.1 - 1
    verticies2[3][0] = transform * -.1 - 1
    glBegin(GL_LINES)
    for idx, edge in enumerate(edges):
        for vertex in edge:
            new_verts = []
            for vert in verticies2[vertex]:
                new_verts.append(vert)
            glVertex3fv(new_verts)
    glEnd()

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -10)

    count = 1
    while True:
        # Quit the "game" with an x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(0, 0, 0, 0) # no movement
        # glRotatef(1, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Cube()
        Cube2(count)
        # redraws the screen
        pygame.display.flip()
        pygame.time.wait(100)
        if count > 20:
            count = 1
        count += 1

main()