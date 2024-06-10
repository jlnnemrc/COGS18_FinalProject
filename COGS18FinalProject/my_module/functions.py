import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def datalist(df, column):
    """
    Displays all the unique values under a specified column in the DataFrame. 
    
    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to be analyzed. 
    column: str
        The name of the column to be analyzed. Must be either 'Carrier' or 'Commitment'.
    
    Returns
    -------
    pandas.DataFrame
        A new DataFrame that contains the unique values under the specified column.
    """
    if column == 'Carrier':
        
            # Because column has repeating values, need to isolate unique values
            carrier_list = df['Carrier'].unique().tolist()
            
            # Displayed output would be clearer through addition of column name
            # So reader would know what data they are looking at
            carrier_df = pd.DataFrame(carrier_list, columns = ['Airline Carrier'])
            
            # Because df index starts at 0, need adjusting for airline amount accuracy
            carrier_df.index = carrier_df.index + 1
            
            return carrier_df
        
    elif column == 'Commitment':
        
            # Output has shortened columns where values are cut and end with ellipsis
            # Need to show full value, thus removing a maximum column width
            pd.options.display.max_colwidth = None
            
            commitments_list = (df['Commitment'].unique()).tolist()
            
            commitments_df = pd.DataFrame(commitments_list, columns = ['Commitment'])
            commitments_df.index = commitments_df.index + 1
            
            return commitments_df

        
def airlines_analysis(df, input):
    """
    Analyzes number of commitments per airline based upon a DataFrame. 
    
    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to be analyzed.
    input: str
        The type of output returned by the function. Must be either 'list' or 'plot'.
    
    Returns
    -------
    pandas.DataFrame or matplotlib.axes.Axes
        If input is 'list': a DataFrame that contains the sorted sum of commitments per airline.
        If input is 'plot': a bar graph that displays the number of commitments per airline.
    """
    # Since there are multiple commitments, need to sum commitments per airline if provided
    airs_sum = df.groupby('Carrier')['Provided'].sum()
    
    # Sorting (ranking) airlines for easier reading of results
    sairs_sum = airs_sum.sort_values(ascending = False)
    
    if input == 'list':
        
        sairs_sum_df = pd.DataFrame(sairs_sum)
        
        return sairs_sum_df
    
    elif input == 'plot':
        
        sairs_plot = sairs_sum.plot(kind = 'bar', color = 'pink')
        sairs_plot.set_title('No. of Commitments per Airline')
        
        # xticks are harder to read if different orientation than general graph, thus need rotating
        plt.xticks(rotation = 45,
                  ha = 'right',
                  color = 'palevioletred')
        
        return sairs_plot

def commitments_analysis(df, input):
    """
    Analyzes number of airlines that provide each commitment based upon a DataFrame. 
    
    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to be analyzed.
    input: str
        The type of output returned by the function. Must be either 'list' or 'plot'.
    
    Returns
    -------
    pandas.DataFrame or matplotlib.axes.Axes
        If input is 'list': a DataFrame that contains the sorted sum of airlines per commitment.
        If input is 'plot': a bar graph that displays the number of airlines per commitment.
    """
    comms_sum = df.groupby('Commitment')['Provided'].sum()
    
    scomms_sum = comms_sum.sort_values(ascending = False)
    
    if input == 'list':
        
        scomms_sum_df = pd.DataFrame(scomms_sum)
        
        return scomms_sum_df
    
    elif input == 'plot':
        
        scomms_plot = scomms_sum.plot(kind = 'bar', color = 'cadetblue')
        scomms_plot.set_title('No. of Airlines per Commitment')
        
        # Default xtick labels contained the entire commitment value (str)
        # Since they were very long, had to be customized and shortened
        tick_labels = []
        for label in scomms_sum.index:
            
            # Limits the labels' number of words into two followed by an ellipsis
            tick_label = (' '.join(label.split()[:2]) + '...')
            tick_labels.append(tick_label)
        
        plt.xticks(range(0, len(scomms_sum.index)), 
                   labels = tick_labels,
                   rotation = 60,
                   ha = 'right',
                   fontsize = 6,
                   color = 'steelblue'
                  )
        
        return scomms_plot