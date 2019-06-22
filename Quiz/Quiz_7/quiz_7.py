# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by ZH Sheng and Eric Martin for COMP9021


from math import pi, hypot
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'

class Disk:
    def __init__ (self , * , centre=Point ( 0 , 0 ) , radius=0):
        self.O = centre
        self.r = radius
        self.area()
    def __repr__(self):
        return f'Disk({self.O}, {self.r:.2f})'
    def area(self):
        self.area = pi * self.r ** 2
    def change_radius (self , new_radius):
        self.r = new_radius
        self.area = pi * self.r ** 2
    def intersects (self , son):
        return hypot ( self.O.x - son.O.x , self.O.y - son.O.y ) <= (self.r + son.r)
    def absorb(self,bigdaddy):
        gap = hypot ( self.O.x - bigdaddy.O.x , self.O.y - bigdaddy.O.y )
        if self.r <= bigdaddy.r:
            if self.r + gap <= bigdaddy.r:
                O_new_x = bigdaddy.O.x
                O_new_y = bigdaddy.O.y
                r_new = bigdaddy.r
            else:
                r_new = (gap + self.r + bigdaddy.r) /2
                O_new_x =  bigdaddy.O.x + (self.O.x - bigdaddy.O.x) * (r_new - bigdaddy.r)  / gap
                O_new_y =  bigdaddy.O.y + (self.O.y - bigdaddy.O.y) * (r_new - bigdaddy.r)  / gap
        else:
            if bigdaddy.r + gap <= self.r:
                O_new_x = self.O.x
                O_new_y = self.O.y
                r_new = self.r
            else:
                r_new = (gap + self.r + bigdaddy.r) / 2
                O_new_x = self.O.x + (bigdaddy.O.x - self.O.x) * (r_new - self.r) / gap
                O_new_y = self.O.y + (bigdaddy.O.y - self.O.y) * (r_new - self.r) / gap
        Disk_new = Disk(centre = Point(O_new_x,O_new_y), radius= r_new)
        return Disk_new




        

            
            
