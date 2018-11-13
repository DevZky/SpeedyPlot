# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:34:55 2018

@author: franzky
"""
import matplotlib.pyplot as plt


def subplots3D(xCol,yCol,zCol,framelist):
    fig = plt.figure(zCol)
    fig.subtitle = f"{xCol}, {yCol}, {zCol}"
    
    zmin=0.85
    zmax=0.96
    
    axes = [fig.add_subplot(221, projection='3d'),
            fig.add_subplot(222, projection='3d'),
            fig.add_subplot(223, projection='3d'),
            fig.add_subplot(224, projection='3d')]
    
    
    for frame in enumerate(framelist):
        x = frame[1][1][xCol]
        y = frame[1][1][yCol]
        z = frame[1][1][zCol]

        p = axes[frame[0]].scatter(x,y,z,cmap="cool",c=z,vmin=zmin,vmax=zmax)

        axes[frame[0]].set_xlabel(xCol)
        axes[frame[0]].set_ylabel(yCol)
        axes[frame[0]].set_zlabel(zCol)
        axes[frame[0]].set_title(frame[1][0])
        
        axes[frame[0]].set_xlim(1000,5000)
        axes[frame[0]].set_ylim(0,200)
        axes[frame[0]].set_zlim(zmin,zmax)
        
        
    fig.colorbar(p)
        
    

if __name__ == "__main__":
    pass
    