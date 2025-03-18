import numpy as np
import pandas as pd
from config import IDs, id_to_body, file_name 


def csv_to_df(file_name):
    # Importing data
    df = pd.read_csv(file_name)
    # IMU IDs
    df = df[df["ID"].isin(IDs)] 

    #TODO: After fixing the sensors' data collection this won't be necassary
    # Replacing the Quat and LAcc values
    df = df.copy()
    df[['Quaternion w', 'Quaternion x', 'Quaternion y']] = df[['Linear Acceleration x','Linear Acceleration y', 'Linear Acceleration z']].values
    df[['Linear Acceleration x','Linear Acceleration y', 'Linear Acceleration z']] = df[['Quaternion w', 'Quaternion x', 'Quaternion y']].values

    ## Joint_name and id_to_body are configured in configF.py ##


    # Create a new column for body part
    df['body_part'] = df['ID'].map(id_to_body)

    df = df.dropna() # Droping the values that have no IDs


    '''
    The below code is for times that the lenght of the IDs are note the same as each other.
    For example for IDs=[2, 12], the IDs in df should be: [2, 12, 2, 12..., 2, 12]    where len(2) = len(12)
    However,sometime we might have uneven number of IDs:  [2, 12, 2, 12..., 2, 12, 2] where len(2) != len(12)
    So the last rows should be omitted until len(2) = len(12)
    '''
    remainder = len(df) % len(IDs)
    if remainder:
        df = df.iloc[:-remainder]

    return df

df = csv_to_df(file_name)