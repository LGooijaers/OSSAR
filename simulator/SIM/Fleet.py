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

#importing the aircraft database
text = open(os.getcwd()+"\\SIM\\aircraft_database.txt","r")
lines = text.readlines()[1:]
data = [lines.split() for lines in lines]
text.close()
#import waypoint database
wp_database_text = open(os.getcwd()+"\\SIM\\waypoint_database.txt","r")
wp_database_lines = wp_database_text.readlines()[1:]
wp_database = [wp_database_lines.split() for wp_database_lines in wp_database_lines]
wp_database_text.close()

#create instances
flightplan_ins = Flightplan()
    
def create_orig_aircraft(max_number,idnumber,listnumber,planes,r): # creates the initial aircraft
    for i in xrange(max_number):                        # add aircraft until the set amount of aircraft is achieved
        planetype = random.randint(0,(len(data)-1))     # pick type from database
        fi = radians(random.randint(0,359))             # starting angles and radius
        z = random.randint(0,r)                         # creating the starting coordinate radius
        x1 = cos(fi) * z                                # starting x-coordinate
        y1 = sin(fi) * z                                # starting y-coordinate
        x0 = x1                                         # Save the x-coordinate of the begin position
        y0 = y1                                         # Save the y-coordinate of the begin position
        theta = random.randint(0,359)                   # choose random starting heading
        x2 = cos(theta) * r                             # final x-coordinate
        y2 = sin(theta) * r                             # final x-coordinate
        flightplan = []                                 # Create a list to save the flightplan in
        heading = False                                 # Set an initial value for the heading     
        planes.append(aircraft(data[planetype][0],float(data[planetype][1]),float(data[planetype][2]),idnumber,x0,y0,x1,y1,x2,y2,listnumber,heading,flightplan,[])) # append plane to list   
        planes[listnumber].flightplan = flightplan_ins.create_flightplan(listnumber+1,planes[listnumber].x_beg,planes[listnumber].y_beg,planes[listnumber].x_des,planes[listnumber].y_des,wp_database,r) #add a flightplan to the aircraft      
        idnumber =  idnumber + 1
        listnumber = listnumber + 1
    return idnumber, listnumber, planes

def create_aircraft(max_number,idnumber,listnumber,planes,r): #creates aircraft when nessecary
    while len(planes[::-1]) < max_number:           # add aircraft if needed
#    for k in xrange(max_number-listnumber):         # add aircraft if needed
        planetype = random.randint(0,(len(data)-1)) # pick type from database
        fi = radians(random.randint(0,359))         # starting angles and radius
        x1 = cos(fi) * r                            # starting x-coordinate (on edge)
        y1 = sin(fi) * r                            # starting y-coordinate (on edge)
        x0 = x1                                     # Save the x-coordinate of the begin position
        y0 = y1                                     # Save the y-coordinate of the begin position
        theta = random.randint(0,359)               # choose angle to determine end coordinates
        x2 = cos(theta) * r                         # final x-coordinate
        y2 = sin(theta) * r                         # final x-coordinate
        heading = False                             # Set an initial value for the heading
        planes.append(aircraft(data[planetype][0],float(data[planetype][1]),float(data[planetype][2]),idnumber,x0,y0,x1,y1,x2,y2,listnumber,heading,[],[])) # append plane to list
        planes[listnumber].flightplan = flightplan_ins.create_flightplan(listnumber+1,planes[listnumber].x_beg,planes[listnumber].y_beg,planes[listnumber].x_des,planes[listnumber].y_des,wp_database,r) #add a flightplan to the aircraft
        idnumber =  idnumber + 1
        listnumber = listnumber + 1
    return idnumber, listnumber, planes

def remove_planes(max_number,idnumber,listnumber,planes,r):     # Remove plane if out of boundsaries and update position in list                                     
    for instance in xrange(len(planes)):    
        if sqrt((planes[instance].x_pos - planes[instance].x_des)**2 + (planes[instance].y_pos - planes[instance].y_des)**2) <= 1000: # Removes a plane when within a certain range of its destination
            del planes[instance]
            instance = instance - 1
            for i in range(len(planes)):
                planes[i].update_listnumber(planes)
            listnumber = listnumber - 1
            idnumber, listnumber, planes = create_aircraft(max_number,idnumber,listnumber,planes,r)
    return planes,idnumber,listnumber,instance
    
def update_aircraft(dt,planes):
    for plane in planes:
        plane.update_pos(dt) #update the position of the airplane
    return