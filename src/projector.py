
import numpy as np
class Point:
    x = 0
    y = 0
    z = 0
    #r = 0
    colour = "red"
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.colour = "red"
        
        




class Camera:
    x = 0
    y = 0
    z = 0
    focal_length = 0
    def _init_(self,x,y,z,f):
        self.x = x
        self.y = y
        self.z = z
        self.focal_length = f


    def retProjected(self,p1):
        xp = self.focal_length * (p1.x-self.x) / (self.focal_length + p1.z-self.z)
        yp = self.focal_length * (p1.y-self.y) / (self.focal_length + p1.z-self.z)

        
        return xp,yp


class Screen:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = np.array([[(0.0, 0.0, 0.0, 0.0) for x in range(width)] for y in range(height)])

    def update(camera, point):
        print("updated bro")

