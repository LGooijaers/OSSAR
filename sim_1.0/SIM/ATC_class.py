'''
Package: ATC
module: main
module dependence: Collision_class

description:
Eleborate description: (link to formulas)

Input:
Output:
'''

#import python modules
from math import *
from collision_class import collision

##create instances
coll_ins = collision()

# using the flightplan, calculates the heading for the plane        
def calc_heading(planes):
    for plane in planes:
        if plane.heading == False:
            x = (float(plane.flightplan[0][0])) - (plane.x_pos)
            y = (float(plane.flightplan[0][1])) - (plane.y_pos)           
            plane.heading = atan2(y,x)
        elif len(plane.flightplan) == 0:
            plane.heading = plane.heading
        else:
            if sqrt((plane.x_pos - float(plane.flightplan[0][0]))**2 + (plane.y_pos - float(plane.flightplan[0][1]))**2)<= 800:
                del(plane.flightplan[0])
                if len(plane.flightplan) != 0:
                    x = (float(plane.flightplan[0][0])) - (plane.x_pos)
                    y = (float(plane.flightplan[0][1])) - (plane.y_pos)           
                    plane.heading = atan2(y,x)
    return

def collision_detection(planes,dt,t,nr_LOS,angles):
    for i in xrange(len(planes)):
        planes,nr_LOS,angles = coll_ins.CPA(planes,i,dt,t,nr_LOS,angles)
    return planes,nr_LOS,angles