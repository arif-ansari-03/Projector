
import numpy as np
class Point:
    x = 0
    y = 0
    z = 0
    #r = 0
    colour = (0,0,0,0)
    def __init__(self,x,y,z,r,g,b,alpha):
        self.x = x
        self.y = y
        self.z = z
        temp = list(self.colour)
        temp[0] = r
        temp[1] = g
        temp[2] = b
        temp[3] = alpha
        self.colour = tuple(temp)
        
        




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

