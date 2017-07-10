#!/usr/bin/env python

import numpy as np

mat=np.genfromtxt("grid.txt",delimiter=" ")

xmax=mat.shape[0]-1
ymax=mat.shape[1]-1

xstart=ystart=0

def span(xstart,ystart,xfactor,yfactor,num):
    ''' Start at [xstart,ystart] and get the product of num consecutive
    entries in a given direction specified by factors:
    (+1,0) vertical, (0,+1) horizontal, (+1,+1) top left to bottom right,
    (+1,-1) top right to bottom left. '''
    return np.product([mat[xstart+z*xfactor,ystart+z*yfactor] for z in range(num)])

current_max=0
for i in range(xmax+1):
    for j in range(ymax+1):
        if i<xmax-2:
            if j>2: current_max=max(span(i,j,+1,-1,4),current_max)
            if j<ymax-2: current_max=max(span(i,j,+1,+1,4),current_max)
            current_max=max(span(i,j,+1,0,4),current_max)
        if j<ymax-2: current_max=max(span(i,j,0,+1,4),current_max)
                   
print int(current_max)
