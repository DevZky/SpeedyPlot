"""
data analysis module for calculating special values for specific data sets

@author: Tobias Franzky
"""


#calculate the average "SZT" for some kind of binary data series (1 and 0)
def calc_szt(series):
    
    flanks = series.diff()
    
