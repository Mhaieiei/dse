# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:36:32 2020

@author: petch
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import re
import numpy as np
import joblib
import pickle


# load column template
with open('columns.pkl', 'rb') as f:
      columns = pickle.load(f)
      
# create function clean_data(df) to do all cleaning
def clean_pipeline(clean_df):
#add kind of condo [>9 floor: high rise, else: low rise]
    clean_df['Kind'] = clean_df['#_Floor'].apply(lambda x: 'high rise' if x > 9 else 'low rise')
    clean_df['Road'] = clean_df['Address_TH'].apply(lambda x: re.findall(r'(ถนน\s?[\u0E00-\u0E7F]+\s?\d?)', x))
    clean_df['Road'] = clean_df['Road'].apply(lambda x: x[0] if len(x)> 0 else np.nan)
    clean_df['Road'] = clean_df['Road'].str.replace(" ", "").str.strip()
    clean_df['Road'] = clean_df['Road'].fillna(np.nan)
    new_area = pd.get_dummies(clean_df['Condo_area'], dummy_na=True, prefix='Area_')
    new_kind = pd.get_dummies(clean_df['Kind'], dummy_na=True, prefix='Kind_')
    new_road = pd.get_dummies(clean_df['Road'], dummy_na=True, prefix='Road_')
    clean_df = pd.concat([clean_df, new_area, new_kind, new_road], axis = 1)
    
    clean_df = clean_df.drop('Address_TH', axis=1)
    clean_df = clean_df.drop('Condo_area', axis=1)
    clean_df = clean_df.drop('Kind', axis=1)
    clean_df = clean_df.drop('Road', axis=1)
    
    
    return clean_df

def get_predict(data):
  
  obj = {
    'Condo_area': data.get('condo-area', 'Bang Kapi'),
    'Address_TH': data.get('address', 'ถนนเสรีไทย'),
    'Year_built': data.get('year', '2009'),
    'Area_m2': data.get('sqm', 4695.5),
    '#_Tower': data.get('tower', 1),
    '#_Floor': data.get('floor', 8),
    'Rental_Yield': data.get('rent-yeild', 5.16),
    'Latitude': data.get('lat', 13.738209),
    'Longtitude': data.get('long', 100.566949),
    'MinDist_Station': data.get('min-dist-station', 1833.883835)
  }

  df = pd.DataFrame(columns = columns)
    
  df_data = pd.DataFrame.from_dict([obj])
  print(df_data['Condo_area'])
  print(df_data['Sale_Price_Sqm'])
  df_data = clean_pipeline(df_data)
  df_concat = pd.concat([df, df_data])
  df_concat = df_concat.fillna(0)
  print(df_concat['Condo_area'])
  print(df_concat['Sale_Price_Sqm'])
  scaler = joblib.load("data_scaler.joblib")
  df_concat = scaler.transform(df_concat)

  rf = joblib.load('rf.joblib')

  price = rf.predict(df_concat)
  
  return {'result': price}









