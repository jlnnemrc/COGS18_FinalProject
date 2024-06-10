import pandas as pd
import numpy as np

class DataSet():
    """
    Reads csv files and stores them into a DataFrame. 
    
    Attributes
    ----------
    file : str
        This is the path to the csv file to be used.
    df: pandas.DataFrame
        This is the resulting DataFrame from the csv file.
    """
    def __init__ (self, file):
        
        self.file = file
        
        self.df = pd.read_csv(self.file)