# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:29:04 2018

@author: franzky
"""


from modules import read_to_dataframes
from modules import test_plot


# Einstellungen für korrekten Datenimport als Funktionsvariablen

dfs = read_to_dataframes.files_to_dataframes("heut",2,dec=".",encode="cp1250",index="Uhrzeit: ")


# Rechenschritte hier einfügen
for element in dfs:
    element[1]["JIR02_AE_Pel    "] *= 0.1







# hier muss definiert werden was vom graphen geplottet werden soll


#erstes Argument muss Liste sein!!!
test_plot.plot_data(dfs[0:2:4],["JIR02_AE_Pel    ","dT_Überhitzung  "])



#
#    plot_data(dataframes)


#    dataframes = files_to_dataframes('IEC 0073.17',15,sheetSlice=[19,45])
#    calculation(dataframes)
            