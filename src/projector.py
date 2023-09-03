import pygame
import numpy as np
import math

class Point:
    #r = 0
    colour = (0,0,0,0)
    def __init__(self,x,y,z,color):
        self.position = (x, y, z)
        self.colour = color
        self.x, self.y, self.z = self.position

    def updatePos(self, newPos):
        x, y, z = newPos
        self.position = x, y, z
        self.x, self.y, self.z = self.position


class Camera:
    x = 0
    y = 0
    z = 0
    focal_length = 0
    def __init__(self,x,y,z,f):
        self.x = x
        self.y = y
        self.z = z
        self.focal_length = f
        self.position = x, y, z


    def retProjected(self,p1):
        xp = self.focal_length * (p1.x-self.x) / (self.focal_length + p1.z-self.z)
        yp = self.focal_length * (p1.y-self.y) / (self.focal_length + p1.z-self.z)

        
        return math.floor(xp),math.floor(yp)

    def updatePos(self, x, y, z):
        self.x, self.y, self.z = self.x + x, self.y + y, self.z + z

        


class Screen:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = np.array([[(0.0, 0.0, 0.0, 0.0) for x in range(width)] for y in range(height)])

    def update(self, camera, points, pygameScreen):
        for point in points:
            x, y = camera.retProjected(point)
            pygame.draw.circle(pygameScreen, point.colour, (math.floor(x+self.width/2),math.floor(y+self.height/2)), 2)


