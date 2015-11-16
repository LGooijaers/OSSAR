'''
Package: FLeet
Module: main
module dependence: aircraft_class, flightplan_class

description: The fleet package manages the aircraft

Input:
Output:
'''

#import modules
from aircraft_class import *
from flightplan_class import *
from ATC_class import ATC
import random as rnd

#import data
from data_import import wp_database
from data_import import ar_database
from data_import import g_database
from data_import import rw_database


def create_aircraft(idnumber,listnumber,planes,ATC_list,r,t,dt): #creates aircraft when nessecary
    for i in xrange(len(ar_database)):               # add aircraft if needed
        if int(ar_database[i][-1]) > (t - 0.5*dt) and int(ar_database[i][-1]) < (t + 0.5*dt):
            ATC_gate = int(rnd.choice(g_database))              # Random select a departure gate of the aircraft
            x1 = float(wp_database[ATC_gate][1])                # starting x-coordinate
            y1 = float(wp_database[ATC_gate][2])                # starting y-coordinate
            ATC_runway = int(rnd.choice(rw_database))           # Random select a runway entrance of the aircraft
            x2 = float(wp_database[ATC_runway][1])              # final x-coordinate
            y2 = float(wp_database[ATC_runway][2])              # final y-coordinate
            speed = float(ar_database[i][1])*0.5144             # choose starting speed
            heading = False                                     # Set an initial value for the heading
            new_plane = aircraft(ar_database[i][0],speed,0,idnumber,x1,y1,x1,y1,x2,y2,listnumber,heading,[],[],ATC_gate)
            planes.append(new_plane) # append plane to list
            ATC_list[ATC_gate].add_plane(new_plane)
#            planes[listnumber].flightplan = flightplan_ins.create_flightplan(listnumber+1,planes[listnumber].x_beg,planes[listnumber].y_beg,planes[listnumber].x_des,planes[listnumber].y_des,wp_database,r) #add a flightplan to the aircraft
            idnumber =  idnumber + 1
            listnumber = listnumber + 1            
    return idnumber, listnumber, planes

def update_aircraft(dt,planes):
    for plane in planes:        #loop through all aircraft
        plane.update_pos(dt)    #update the position of each aircraft

def ATC_check(ATC_list,dijk,dt,t,v_max):
    for atc in ATC_list:
        atc.create_commands(ATC_list, commands,v_max,dijk,dt,t)
    return commands

def execute_commands(commands, planes,t,dt):
    execute = [elem for elem in commands if elem[-1] < (t+dt)] # make list of all commands that have to be excecuted this timestep
    for i in xrange(len(execute)):
        for j, plane in enumerate(planes):
            if plane.id == commands[i][1]:
                plane.execute_command(commands[i])          
    commands = [elem for elem in commands if elem[-1] >= (t+dt)]
    return commands,planes

#    for i in xrange(len(commands)):
#        if commands[i][-1] <= dt:        #check wether the command has to be excecuted directly
#            for j, plane in enumerate(planes): #find the correct aircraft for which the command is valid
#                if plane.id == commands[i][0]:             
#        #            if commands[i][0] == 1:
#                    planes[j].speed = commands[i][1]
#                    planes[j].heading = commands[i][2]
#                    planes[j].atc = commands[i][3]
#            commands[i][-1] = commands[i][-1] - dt #change timestamp of each command
#            if commands[i][-1] == -1:   #remove command if it is excecuted (t = negative)
#                commands[i] = []
#    commands = [x for x in commands if x != []]
#    return commands, planes