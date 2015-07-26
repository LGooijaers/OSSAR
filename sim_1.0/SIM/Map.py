'''
Package: Map
Module: main

description: The Map package provides a graphical representation of the simulator

Input:
Output:
'''
import pygame as pg
from math import *

#initializing values
piclist = []
rectlist = []

def map_initialization():
    pg.init()
    reso = (600,600)
    scr = pg.display.set_mode(reso)
    scrrect = scr.get_rect()
    scr.fill((2,255,70))
    plane_pic= pg.image.load("blue-plane-hi.png")
    for i in xrange(0,360):
        piclist.append(pg.transform.rotozoom(plane_pic,i,(1./12.)))
        rectlist.append(piclist[i].get_rect())
    return reso, scr, scrrect, plane_pic, piclist
    
def map_running(reso,scr,scrrect,plane_pic,piclist,planes,rectlist,running,r):
    pg.draw.rect(scr,(255,255,255),scrrect)
    pg.draw.circle(scr,(255,0,0),(reso[0]/2,reso[1]/2),reso[0]/2, 3)
    for i in xrange(len(planes)):
        deg = int(degrees(planes[i].heading)-90)
        rectlist[deg].centerx = int((planes[i].x_pos + r)/ (2*r) * reso[0])
        rectlist[deg].centery = int((planes[i].y_pos - r)/ (2 * r) *reso[1]) * -1
        scr.blit(piclist[deg],rectlist[deg])
    pg.display.flip()
    pg.event.pump()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False
        print 'abort'
    return running