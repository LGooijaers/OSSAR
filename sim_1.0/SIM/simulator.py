'''
Main simulator

description: The Main simulator simulates airtraffic in an predifined airspace for a set amount of time. Depending on the added packages the ouput can differ.

Input: Fleet package, ATC_class package, Map package

'''

#import packages
from Fleet import *
from ATC_class import *
from Map import *

#import python modules
from numpy import *
import random
from math import *
import pygame as pg

def simrun(max_number,t_sim,area,dt,Map):
    #initializing values
    listnumber = 0
    idnumber = 0
    t = 0
    efficiency = []
    planes = []
    angles = []
    nr_LOS = 0
    running = True
    #creating the radius of the airspace
    r = int(1000.0 * np.sqrt(area/np.pi))    

    if Map == 'on':
        reso, scr, scrrect, plane_pic, piclist = map_initialization()

    #initializing
    create_orig_aircraft(max_number, idnumber, listnumber,planes, r)   
    
    #simulator loop    
    while running == True:
        #clock
        t = t + dt
        #check wether the plains have arrived at their destination
        planes,idnumber,listnumber,instance = remove_planes(max_number,idnumber,listnumber,planes,r)
        #If necessary, update the heading of each plane
        calc_heading(planes)
        #update the aicraft position
        update_aircraft(dt,planes)
        #detect wether collsions happened this timestep
        planes,nr_LOS,angles = collision_detection(planes,dt,t,nr_LOS,angles)
        
        if Map == 'on':
            running = map_running(reso,scr,scrrect,plane_pic,piclist,planes,rectlist,running,r)
        if t>= t_sim:
            running = False
            
    if Map == 'on':
        pg.quit()
    
    nr_CLOS = 0
    nr_NMAC = 0
    nr_MAC = 0 
    return nr_LOS,nr_CLOS,nr_NMAC,nr_MAC,planes,angles
