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

# Aircraft class is created
class aircraft:

    # Properties of the aircraft 
    def __init__(self,Type,Speed,Range,Number,X0,Y0,X1,Y1,X2,Y2,listnumber,heading,flightplan,col_list,ATC_id):
        self.t = Type
        self.v = Speed
        self.r = Range
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
        self.atc = ATC_id
        return

    # Update positions using velocity and heading (heading is obtained from ATC)
    def update_pos(self,dt):                                           
        self.x_pos = self.x_pos + self.v * dt * cos(self.heading)
        self.y_pos = self.y_pos + self.v * dt * sin(self.heading)
        return 

    # Update position in list 
    def update_listnumber(self, planes):                                             
        listid = []
        for i in range(len(planes)):
            listid.append(planes[i].id)
        self.listnumber = listid.index(self.id)
        return

    def execute_command(self,command): #execute commands given to this aircraft this timestep
        if command[0] ==1:
            self.change_speed(command[2])
        if command[0] ==2:
            self.change_heading(command[2])
        if command[0] ==3:
            self.change_atc(command[2])
#        [commandtype, plane.id, plane.atc, time]

    def change_speed(self,new_speed):
        self.v = new_speed

    def change_heading(self,new_heading):
        self.heading = new_heading
        
    def change_atc(self,new_atc):
        self.atc = new_atc


#    def execute_command(self,command,par):
#        return {
#            'change_speed': self.change_speed(par),
#            'change_heading': self.change_heading(par),
#            'change_atc': self.change_atc(par)
#        }
#
#    def change_speed(self,par):
#        self.v = par.v
#
#    def change_heading(self,par):
#        self.heading = par.heading
#        
#    def change_atc(self,par):
#        self.atc = par.atc