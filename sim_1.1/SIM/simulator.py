'''
Main simulator

description: The Main simulator simulates airtraffic in an predifined airspace for a set amount of time. Depending on the added packages the ouput can differ.

Input: Fleet package, ATC_class package, Map package

'''

#import packages
from Fleet import *
from ATC_class import ATC
from Map import *

#import python modules
from numpy import *
import random
from math import *
import pygame as pg

#import data
from data_import import wpl_database

def simrun(max_number,t_sim,area,dt,Map):
    #initializing values
    listnumber = 0
    idnumber = 0
    t = 0
#    nr_LOS = 0
#    efficiency = []
#    angles = []
    planes = []
    ATC_list = []
    commands = []
    running = True
    r = int(1000.0 * np.sqrt(area/np.pi))   #creating the radius of the airspace
    #determine the maximum speed which can be achieved throughout the simulation
    v_list = [ar_database[x][1] for x in range(len(ar_database))]
    v_max = max(map(float,v_list))*0.5144
    
    if Map == True:
        reso, scr, scrrect, plane_pic, piclist, X_waypoint, Y_waypoint = map_initialization(wp_database)
        
    # create ATC for each waypoint
    for i in xrange(len(wp_database)):
        ATC_linkpare = [elem for elem in wpl_database if int(elem[0]) == i] #makes a list of all links for this ATC
        ATC_link = [int(x[1]) for x in ATC_linkpare] # makes a list of all possible destination waypoints
        ATC_list.append(ATC(wp_database[i][0],ATC_link,[],int(wp_database[i][3]),float(wp_database[i][1]),float(wp_database[i][2]),[]))
   
    #simulator loop    
    while running == True:
        idnumber,listnumber,planes = create_aircraft(idnumber,listnumber,planes,ATC_list,r,t,dt) #create new aircraft if nessecary

        commands = ATC_check(ATC_list,commands,dt,t,v_max) # check for new commands from the ATC
        commands, planes = execute_commands(commands, planes,t,dt) # excecute all commands
        update_aircraft(dt,planes) #update the aicraft position
#        planes,nr_LOS,angles = collision_detection(planes,dt,t,nr_LOS,angles) #detect wether collsions happened this timestep

        if Map == True:
            running = map_running(reso,scr,scrrect,plane_pic,piclist,ATC_list,rectlist,running,r,X_waypoint,Y_waypoint,wp_database)
        if t>= t_sim:
            running = False

        t = t + dt # update clock
    if Map == True:
        pg.quit()
    
#    nr_CLOS = 0
#    nr_NMAC = 0
#    nr_MAC = 0 
#    return nr_LOS,nr_CLOS,nr_NMAC,nr_MAC,planes,angles
    return
