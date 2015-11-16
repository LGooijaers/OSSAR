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
import random as rnd
from data_import import wp_database
#from collision_class import collision

##create instances
#coll_ins = collision()

class ATC:
    
    def __init__(self, ATC_ID, ATClink, locplanes, ATCtype, x_handoff, y_handoff, commandlist):
        self.id = ATC_ID                #ATC identification number
        self.link = ATClink             #Array of possible handover ATC
        self.locp = locplanes           #Array of planes under command
        self.type = ATCtype             #Type of ATC (gate(1), waypoint(2), end(4))
        self.x_handoff = x_handoff      #x-coordinate at which a aircraft should be handed over
        self.y_handoff = y_handoff      #y-coordinate at which a aircraft should be handed over
#        self.cmdlist = commandlist      #list of commands

    def create_commands(self, ATC_list, commands,v_max,dt,t):
#       command types:
#           -speed = 1
#           -heading = 2
#           -atc = 3
        for plane in self.locp:
            # check if plane across threshold to pass on to next ATC
            if sqrt((plane.x_pos - self.x_handoff)**2 + (plane.y_pos - self.y_handoff)**2) <= v_max*dt: #check wether the aircraft is within range of its next destination ((v_max*dt))
                if self.type == 1:  #check to which type of ATC the aircraft is assigned
                    self.plane_handoff(ATC_list, plane, commands,t)
                elif self.type == 2:
                    self.plane_handoff(ATC_list, plane, commands,t)
                elif self.type == 4:
                    self.remove_plane(plane)

    def plane_handoff(self,ATC_list,plane, commands,t):
          # select next ATC randomly ...this where Dijkstra will come in
            next_atc = int(rnd.choice(self.link))
            plane.atc = next_atc
            
            ATC_list[next_atc].add_plane(plane) # add to next ATC
            self.remove_plane(plane) # remove from current ATC
            commandtype = 3         #set command type (3 ~ atc change)
            commands.append([commandtype, plane.id, plane.atc, t])

            plane.heading = atan2((int(wp_database[int(plane.atc)][2])-(plane.y_pos)), (int(wp_database[int(plane.atc)][1])-(plane.x_pos)))
            commandtype = 2         #set command type (2 ~ heading change)
            commands.append([commandtype, plane.id, plane.heading, t])             
#            commands.append([plane.id, plane.v, plane.heading, plane.atc, time])

    def remove_plane(self,plane):
        self.locp.remove(plane)
#        print 'Removed from atc: ' + str(self.id)

    def add_plane(self,plane):
        self.locp.append(plane)
#        print 'Added to WP ' + str(self.id)
        
# using the flightplan, calculates the heading for the plane        
#    def calc_heading(planes):
#        for plane in planes:
#            if plane.heading == False:
#                x = (float(plane.flightplan[0][0])) - (plane.x_pos)
#                y = (float(plane.flightplan[0][1])) - (plane.y_pos)           
#                plane.heading = atan2(y,x)
#            elif len(plane.flightplan) == 0:
#                plane.heading = plane.heading
#            else:
#                if sqrt((plane.x_pos - float(plane.flightplan[0][0]))**2 + (plane.y_pos - float(plane.flightplan[0][1]))**2)<= 800:
#                    del(plane.flightplan[0])
#                    if len(plane.flightplan) != 0:
#                        x = (float(plane.flightplan[0][0])) - (plane.x_pos)
#                        y = (float(plane.flightplan[0][1])) - (plane.y_pos)           
#                        plane.heading = atan2(y,x)
#        return
    
#    def collision_detection(planes,dt,t,nr_LOS,angles):
#        for i in xrange(len(planes)):
#            planes,nr_LOS,angles = coll_ins.CPA(planes,i,dt,t,nr_LOS,angles)
#        return planes,nr_LOS,angles