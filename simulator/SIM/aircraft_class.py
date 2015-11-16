'''
Package: FLeet
Module: aircraft

description: This module makes it possible to create aircraft as instances

Input:
Output:

Package dependence:
'''

#Import python modules
import numpy as np
import random
from math import *
from ATC_class import *
import os

# Aircraft class is created
class aircraft:

    # Properties of the aircraft 
    def __init__(self,Type,Speed,Range,Number,X0,Y0,X1,Y1,X2,Y2,listnumber,heading,flightplan,col_list):
        self.v = Speed
        self.r = Range
        self.t = Type
        self.id = Number
        self.x_beg = X0
        self.y_beg = Y0
        self.x_pos = X1
        self.y_pos = Y1
        self.x_des = X2
        self.y_des = Y2
        self.listnumber = listnumber
        self.heading = heading
        self.flightplan = flightplan
        self.col_list = col_list
        return

    # Update positions using velocity and heading (heading is obtained from ATC)
    def update_pos(self,dt):                                           
        self.x_pos = self.x_pos + self.v * dt * cos(self.heading)
        self.y_pos = self.y_pos + self.v * dt * sin(self.heading)
        return 

    # Updat position in list 
    def update_listnumber(self, planes):                                             
        listid = []
        for i in range(len(planes)):
            listid.append(planes[i].id)
        self.listnumber = listid.index(self.id)
        return

    # Remove plane if out of bounds and update position in list 
    def remove_plane(self,idnumber,listnumber,instance,planes,r):                                         
        if sqrt((self.x_pos - self.x_des)**2 + (self.y_pos - self.y_des)**2) <= 1000: # Removes a plane when within a certain range of its destination
            del planes[instance]
            instance = instance - 1
            for i in range(len(planes)):
                planes[i].update_listnumber(planes)
            listnumber = listnumber - 1
            idnumber, listnumber, planes = create_aircraft(max_number,idnumber,listnumber,planes,r)
        return planes,idnumber,listnumber,instance