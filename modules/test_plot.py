# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:40:54 2018


Sensor Bezeichungen:
    
    ["T Top","TKF oben","TKF mitte","TKF unten","TKLF o","TKLF m","TKLF u"]
    
    ["TKF oben", "TKF mitte", "TKF unten", "TKF o", "TKF m", "TKF u"]
    
    ["P", "Compressor", "TSR"]


@author: franzky
"""

import matplotlib.pyplot as plt

#from matplotlib.widgets import CheckButtons
#from matplotlib.font_manager import FontProperties

    
def plot_data(dataframes, column_names,rangeargs=None):
   
    
    #for i in range(rangeargs[0],rangeargs[1],rangeargs[2]):    
    if rangeargs == None:
        
        for i in dataframes:
            df = i
            #df[1]["Energie"] /= 1000000
           
            #for element in [["TKF mitte","P"],["Compressor","DefrostHeater", "CCompFan" ,"CCompEvapSensor", "CCompSensor", "FgCompSensor"]] :
            #    plt.figure()
            #    df[1][element].plot(grid=True)
            #    plt.suptitle(df[0])
            #    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fancybox=True, shadow=True)
            #    plt.show()
            #    plt.tight_layout(rect=[0,0,1,0.95])
        
            try:            
                df[1][column_names].plot(grid=True, drawstyle="steps-mid", linewidth=1, title = df[0])
                plt.minorticks_on()
                plt.grid(b=True, which="both")
                plt.grid(which='minor', linewidth='0.5', color='lightgrey')        
                plt.rcParams['figure.figsize'] = (12, 5)
                plt.show()
                plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fancybox=True, shadow=True) 
                plt.tight_layout(rect=[0,0,1,0.95])
            except:
                print("for # {} # at least one wrong column declared".format(df[0]))
                pass
        
            # Shrink current axis by 20%
            #ax = plt.subplot(111)
            #box = ax.get_position()
            #ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    
if __name__=="__main__":    
    pass