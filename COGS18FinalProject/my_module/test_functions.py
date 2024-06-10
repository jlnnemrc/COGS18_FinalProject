import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pytest
import pandas.testing as pdt

from my_module.functions import datalist, airlines_analysis, commitments_analysis
from my_module.classes import DataSet

df = pd.DataFrame({
    'Carrier': ['A', 'B', 'C', 'D'],
    'Commitment': ['1', '2', '3', '4'],
    'Provided': [0, 1, 1, 0]
    })

def test_datalist():
    assert callable(datalist)
    assert type((datalist(df, 'Carrier'))) == pd.DataFrame
    assert type((datalist(df, 'Commitment'))) == pd.DataFrame
    
    # To test for carrier column
    result_df1 = datalist(df, 'Carrier')
    expected_df1 = pd.DataFrame({'Airline Carrier' : ['A', 'B', 'C', 'D']}, index = [1, 2, 3, 4])
    
    pdt.assert_frame_equal(result_df1, expected_df1)

    # To test for commitment column
    result_df2 = datalist(df, 'Commitment')
    expected_df2 = pd.DataFrame({'Commitment': ['1', '2', '3', '4']}, index = [1, 2, 3, 4])

    pdt.assert_frame_equal(result_df2, expected_df2)
    
def test_airlines_analysis():
    assert callable(airlines_analysis)
    assert type((airlines_analysis(df, 'list'))) == pd.DataFrame
    assert type((airlines_analysis(df, 'plot'))) == matplotlib.axes.Axes
    
    result_df3 = airlines_analysis(df, 'list')
    expected_df3 = pd.DataFrame({'Provided': [0, 1, 1, 0]}, index=['A', 'B', 'C', 'D'])
    expected_df3.index.name = 'Carrier'

    pdt.assert_frame_equal(result_df3.sort_index(), expected_df3.sort_index())

def test_commitments_analysis():
    assert callable(commitments_analysis)
    assert type((commitments_analysis(df, 'list'))) == pd.DataFrame
    assert type((commitments_analysis(df, 'plot'))) == matplotlib.axes.Axes
    
    result_df4 = commitments_analysis(df, 'list')
    expected_df4 = pd.DataFrame({'Provided': [0, 1, 1, 0]}, index=['1', '2', '3', '4'])
    expected_df4.index.name = 'Commitment'

    pdt.assert_frame_equal(result_df4.sort_index(), expected_df4.sort_index())