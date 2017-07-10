#!/usr/bin/env python

import numpy as np

mat=np.genfromtxt("grid_dummy.txt",delimiter=" ")

xmax=mat.shape[0]-1
ymax=mat.shape[1]-1

xstart=ystart=0

# horizontal
def horizontal(mat, x, y):
    return mat[x,y]*mat[x,y+1]*mat[x,y+2]*mat[x,y+3]
    
# vertical
def vertical(mat, x, y):
    return mat[x,y]*mat[x+1,y]*mat[x+2,y]*mat[x+3,y]

# diagonal TL to BR
def diagTLBR(mat, x, y):
    return mat[x,y]*mat[x+1,y+1]*mat[x+2,y+2]*mat[x+3,y+3]

# diagonal TR to BL
def diagTRBL(mat, x, y):
    return mat[x,y]*mat[x+1,y-1]*mat[x+2,y-2]*mat[x+3,y-3]

current_max=0
for i in range(xmax+1):
    for j in range(ymax+1):
        if i<xmax-2:
            if j>2: current_max=max(diagTRBL(mat,i,j),current_max)
            if j<ymax-2: current_max=max(diagTLBR(mat,i,j),current_max)
            current_max=max(vertical(mat,i,j),current_max)
        if j<ymax-2: current_max=max(horizontal(mat,i,j),current_max)
                   
print int(current_max)
