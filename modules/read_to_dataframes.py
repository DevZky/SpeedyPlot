# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:39:14 2018

module for reading Data in .csv-files to dataframes

@author: franzky
"""

import os, sys
import pandas as pd

# sheetSlice argument should be obsolet in next version, due to the possibility to rename the .csv files before reading

def files_to_dataframes(strFileStart, nSkip, index="Zeit",seperator = "\t", dec = "," ,encode = None,excel=False, xlsxName = "measurements.xlsx", sheetSlice = [0,10] ):
    # command for re<ding special character in filenames
    sys._enablelegacywindowsfsencoding()
    
    files = []
    dataframes = []
    
    # get path of curretn script file as string
    path = sys.argv[0]
    path = "/".join(path.split("/")[:-1]) + "/"
    
    
    # extends list with file strings of a specific start string
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and strFileStart in i:
            files.append(i)
    
    
    for filename in files:
        # append label as string and corresponding dataframe to list dataframes
        dataframes.append([filename,pd.read_csv(filename, skiprows=nSkip, sep = seperator, decimal=dec, encoding = encode, index_col=index)])
    
    #print read values to excelfile
    if excel==True:
        writer = pd.ExcelWriter(xlsxName)
        for i in range(0,len(dataframes)):
            dataframes[i][1].to_excel(writer,"{}".format(dataframes[i][0][sheetSlice[0]:sheetSlice[1]]))
        writer.save()
    

    return dataframes

if __name__ == "__main__":
    dataframes = files_to_dataframes('IEC 0073.17',15,sheetSlice=[19,45],encode="utf_16_le")
    