import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,MultiComparison)
from pandas.plotting import table 
import folium
from pytablewriter import MarkdownTableWriter

def mean_confidence_interval(df):
    mean = df.mean()
    se = df.sem()
    CI = stats.t.interval(0.95, len(df)-1, loc=mean, scale=se)
    
    return mean, CI[1]-mean

def Create_mdTable(df): 
    ''' I use this function to create MD style tables 
    '''   
    writer = MarkdownTableWriter()
    writer.from_dataframe(df)
    

    return writer.write_table()

def map_marker(latitude,longitude,rad ,color ='red',fill_color='red'):
    marker = folium.CircleMarker(
    location=[latitude, longitude],
    radius=rad/1000,
    color=color,
    fill=True,
    fill_color=fill_color
    )
    return marker

def add_marker(df,folium_map):
    for i in range(0,len(df)):    
        df.marker.iloc[i].add_to(folium_map)
    return folium_map    

def grouby_function (df,lstGroup,d):
    ''' df : A pandas dataframe
        lstGroup: list of all the features that should be grouped by. 
        emaple for lstGroup: ['Year','Month']
        d: a dictionary including new column name, agg function,
        and name of the column that you want to agg on it
        eample: d = {'Total_count_day': pd.NamedAgg(column='starttime', aggfunc='count')} 
    '''
    
    return df.groupby(lstGroup).agg(**d).reset_index()