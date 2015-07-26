'''
Package: ATC
module: Collision detection

description: This module uses CPA to detect conflicts between aircraft

Input:
Output:

Package dependence:
'''

#import python modules
from math import *
from numpy import *


class collision:
    
    def __init__(self):
        return
        
    def CPA(self,planes,l,dt,t_total,nr_LOS,angles):
        j = l + 1
        if j <= len(planes):
            while j < len(planes):
                d = sqrt((planes[j].x_pos - planes[l].x_pos)**2 + (planes[j].y_pos - planes[l].y_pos)**2)          
                if d <= 15000:
                    P_start = matrix([[planes[j].x_pos],
                                     [planes[j].y_pos]])
                                     
                    Q_start = matrix([[planes[l].x_pos],
                                         [planes[l].y_pos]])
                      
                    t_start = t_total
                
                    t_out = t_start + dt
                    V = matrix([[planes[j].v * cos(planes[j].heading)],[planes[j].v * sin(planes[j].heading)]])
                    
                    U = matrix([[planes[l].v * cos(planes[l].heading)],[planes[l].v * sin(planes[l].heading)]])
                    
                    A = (V[0,0] - U[0,0])**2 + (V[1,0] - U[1,0])**2
                    B = 2*P_start[0,0]*(V[0,0]-U[0,0]) + 2*Q_start[0,0]*(U[0,0]-V[0,0]) + 2*P_start[1,0]*(V[1,0]-U[1,0]) + 2*Q_start[1,0]*(U[1,0]-V[1,0])
                    C = (P_start[0,0]-Q_start[0,0])**2 + (P_start[1,0]-Q_start[1,0])**2
                    t_cpa = - B / (2.*A)
                    
                    if dt < t_cpa:
                        t_cpa = dt
                
                    if t_cpa < 0:
                        t_cpa = 0.0 
                
                    dist =  sqrt(A*t_cpa**2 + B*t_cpa + C)
                    angle = arccos((V[0,0]*U[0,0]+V[1,0]*U[1,0]) /(sqrt(V[0,0]**2+V[1,0]**2)*sqrt(U[0,0]**2+U[1,0]**2)))
                    if dist <= 9260.:
#                        Type = "LOS"
                        if planes[j].id not in planes[l].col_list:
                            planes[j].col_list.append(planes[l].id)                         
                            planes[l].col_list.append(planes[j].id)
                            angles.append(angle)
                            nr_LOS = nr_LOS + 1
                            
    #            elif 152.4 <= dist < 2037.2:
    #                Type = "CLOS"
    #                if (planes[j].id,Type) not in planes[listnumber].col_list:
    #                    planes[j].col_list.append((planes[listnumber].id,Type))                         
    #                    planes[listnumber].col_list.append((planes[j].id,Type))
    #                    nr_CLOS = nr_CLOS +1
                        
    #            elif 30.48 <= dist < 152.4:
    #                Type = "NMAC"
    #                if (planes[j].id,Type) not in planes[listnumber].col_list:
    #                    planes[j].col_list.append((planes[listnumber].id,Type))                         
    #                    planes[listnumber].col_list.append((planes[j].id,Type))
    #                    
    #            elif dist < 30.48:
    #                Type = "MAC"
    #                if (planes[j].id,Type) not in planes[listnumber].col_list:
    #                    planes[j].col_list.append((planes[listnumber].id,Type))                         
    #                    planes[listnumber].col_list.append((planes[j].id,Type))
                j = j + 1                
                
        return planes, nr_LOS, angles

